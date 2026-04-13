import streamlit as st
import requests

st.title("AI Resume ATS")

resume = st.text_area("Resume")
jd = st.text_area("Job Description")

if st.button("Analyze"):
    res = requests.post("http://localhost:8001/analyze",
                        json={"resume": resume, "jd": jd})
    st.write(res.json())