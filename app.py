import streamlit as st
from matcher import compute_match_score

st.set_page_config(page_title="Resume-JD Matcher", layout="centered")

st.title("Resume vs Job Description Matcher")
st.markdown("Paste your **Resume** and **Job Description** below to get a match score.")

resume_text = st.text_area("Paste your Resume:", height=250)
jd_text = st.text_area("Paste the Job Description:", height=250)

if st.button("Compute Match Score"):
    if resume_text.strip() and jd_text.strip():
        score = compute_match_score(resume_text, jd_text)
        st.success(f" Match Score: {score} %")
    else:
        st.warning("Please enter both the resume and the job description.")
