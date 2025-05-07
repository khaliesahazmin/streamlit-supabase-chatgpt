# 📄 Streamlit Supabase ChatGPT App

A fully functional Streamlit app that allows users to upload documents (PDF, Word, Excel, Images), extract text using OCR or parsing tools, analyze the content using OpenAI's ChatGPT, and optionally store the results in a Supabase PostgreSQL database.

---

## ✨ Features

- 🖼 Upload and extract text from PDFs, Word documents, Excel sheets, and images.
- 🤖 Analyze and summarize extracted content with ChatGPT (GPT-4).
- 🗃 Save extracted data and metadata to Supabase.
- 🔐 Secure credentials using `.streamlit/secrets.toml`.
- ☁️ Deployable on Streamlit Cloud with GitHub integration.

---

## 📂 Supported File Types

- `.pdf` – Multi-page PDF files using PyMuPDF
- `.docx` – Word documents using `python-docx`
- `.xlsx` – Excel spreadsheets using `pandas`
- `.png`, `.jpg`, `.jpeg` – Images using OCR (`pytesseract`)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/khaliesahazmin/streamlit-supabase-chatgpt.git
cd streamlit-supabase-chatgpt
