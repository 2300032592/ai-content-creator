import streamlit as st
from model import generate_content
from prompt_analyzer import analyze
from dotenv import load_dotenv
import os  # <-- add

# Load environment variables
load_dotenv()

st.title("AI Content Generator - Milestone 2")
st.caption(f"Running: {__file__}")   # <-- add
st.caption(f"CWD: {os.getcwd()}")    # <-- add

# ...existing code...
content_type = st.selectbox(
    "Select content type:",
    ["LinkedIn Post", "Ad Copy", "Professional Email", "Conversational Text"],
)

col1, col2, col3 = st.columns(3)
with col1:
    tone = st.selectbox("Tone", ["Auto", "Professional", "Casual", "Persuasive", "Friendly"], index=0)
with col2:
    length = st.selectbox("Length", ["Short", "Medium", "Long"], index=1)
with col3:
    audience = st.selectbox("Audience", ["General", "B2B", "B2C", "Technical", "Non-technical"], index=0)

prompt = st.text_area("Enter your prompt")
auto = st.checkbox("Auto-detect tone/audience/keywords from prompt", value=True)

if st.button("Generate"):
    detected = analyze(prompt) if auto else {"tone": None, "length": length, "audience": audience, "keywords": []}
    eff_tone = None if tone == "Auto" else tone
    if auto and not eff_tone:
        eff_tone = detected["tone"]
    eff_length = detected["length"] if auto else length
    eff_audience = detected["audience"] if auto else audience
    keywords = detected.get("keywords", [])

    st.write("## Output:")
    try:
        output = generate_content(prompt, content_type, eff_tone, eff_length, eff_audience, keywords)
        st.success(output)
    except Exception as e:
        st.error(f"Error: {e}")