from supabase import create_client
import streamlit as st

url = st.secrets["supabase_url"]
key = st.secrets["supabase_key"]
supabase = create_client(url, key)

def insert_document(filename, content):
    data = {"filename": filename, "content": content}
    supabase.table("documents").insert(data).execute()
