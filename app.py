import streamlit as st
from extractor.parser import extract_text_from_pdf
from extractor.extractor import extract_info

st.set_page_config(page_title="Resume Skill Extractor", layout="centered")
st.title("📄 Resume Skill Extractor")

uploaded_file = st.file_uploader("Upload your resume (PDF only)", type="pdf")

if uploaded_file:
    with open("uploaded_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    text = extract_text_from_pdf("uploaded_resume.pdf")
    info = extract_info(text)

    st.subheader("🔍 Extracted Information")
    for key, value in info.items():
        st.markdown(f"**{key.capitalize()}**: {value}")
