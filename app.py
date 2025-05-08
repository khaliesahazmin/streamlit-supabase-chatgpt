import streamlit as st
from io import BytesIO
from PIL import Image
import pandas as pd
import pytesseract
import fitz  # PyMuPDF
from docx import Document
from supabase import create_client, Client
import os

# Load Supabase credentials (or use st.secrets)
url = "https://ffveploxghexwswvaiur.supabase.co" 
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZmdmVwbG94Z2hleHdzd3ZhaXVyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDY2NjEwMjksImV4cCI6MjA2MjIzNzAyOX0.F6HWiDl2hKpr6xd4boKWD6C7ooo-DMdMttGeC5LyQ9M" 
supabase: Client = create_client(url, key)

st.title("📄 Universal Document Reader with ChatGPT + Supabase")

uploaded_file = st.file_uploader("Upload a file (PDF, Word, Excel, Image)", type=["pdf", "docx", "xlsx", "jpg", "png"])

def extract_text(file, filename):
    ext = filename.split(".")[-1].lower()

    if ext in ["jpg", "jpeg", "png"]:
        image = Image.open(file)
        return pytesseract.image_to_string(image)

    elif ext == "pdf":
        text = ""
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        return text if text.strip() else "PDF contains no extractable text."

    elif ext == "docx":
        doc = Document(file)
        return "\n".join([p.text for p in doc.paragraphs])

    elif ext == "xlsx":
        df = pd.read_excel(file)
        return df.to_string(index=False)

    return "Unsupported file type"

if uploaded_file:
    filename = uploaded_file.name
    text = extract_text(uploaded_file, filename)

    st.subheader("Extracted Text")
    st.text_area("Text", text, height=300)

    if st.button("Save to Supabase"):
        supabase.table("documents").insert({"filename": filename, "content": text}).execute()
        st.success("✅ Document saved to Supabase!")

import openai

openai.api_key = st.secrets["openai_api_key"]

if st.button("Send to ChatGPT"):
    with st.spinner("Analyzing..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": f"Please summarize this document:\n\n{text}"}
            ]
        )
        answer = response.choices[0].message.content
        st.subheader("🔍 ChatGPT Analysis")
        st.write(answer)
