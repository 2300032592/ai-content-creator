import streamlit as st
from model import generate_content
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.title("AI Content Generator - Milestone 1")

content_type = st.selectbox(
    "Select content type:",
    ["LinkedIn Post", "Ad Copy", "Professional Email", "Conversational Text"]
)

prompt = st.text_area("Enter your prompt")

if st.button("Generate"):
    st.write("## Output:")
    output = generate_content(prompt, content_type)
    st.success(output)