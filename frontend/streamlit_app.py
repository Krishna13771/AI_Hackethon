import streamlit as st
import requests
import json

# -------- PAGE SETTINGS --------
st.set_page_config(page_title="AI Resume Generator", page_icon="📝", layout="wide")

# -------- CORPORATE UI CSS --------
st.markdown("""
<style>

    body, .main {
        background: linear-gradient(135deg, #E8EDF3, #F7F9FC);
        font-family: 'Inter', sans-serif;
        color: #1F2937;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .title {
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        color: #1F2937;
        margin-bottom: -5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #4B5563;
        margin-bottom: 40px;
    }

    .card {
        background: #FFFFFF;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 4px 14px rgba(0,0,0,0.06);
        margin-bottom: 25px;
        transition: 0.2s ease;
    }

    .card:hover {
        box-shadow: 0 6px 20px rgba(0,0,0,0.10);
        transform: translateY(-3px);
    }

    .section-title {
        font-size: 18px;
        font-weight: 700;
        color: #2563EB;
        margin-bottom: 12px;
    }

    input, textarea {
        background: #F9FAFB !important;
        border-radius: 10px !important;
        color: #1F2937 !important;
        border: 1px solid #D1D5DB !important;
    }

    input:focus, textarea:focus {
        border: 1px solid #2563EB !important;
        box-shadow: 0 0 6px rgba(37, 99, 235, 0.3);
    }

    label {
        color: #374151 !important;
        font-weight: 600 !important;
    }

    .stButton>button {
        background: #2563EB;
        color: white;
        padding: 14px 24px;
        font-size: 17px;
        font-weight: 600;
        border-radius: 10px;
        border: none;
        width: 100%;
        transition: 0.2s ease;
    }

    .stButton>button:hover {
        background: #1D4ED8;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
        transform: translateY(-2px);
    }

    .download {
        font-size: 20px;
        font-weight: 600;
        color: #2563EB;
        text-decoration: none;
    }

    .download:hover {
        color: #1D4ED8;
        text-decoration: underline;
    }

</style>
""", unsafe_allow_html=True)

# ----- TITLE -----
st.markdown("<div class='title'>AI Resume Generator</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Generate a professional, ATS-friendly resume instantly</div>", unsafe_allow_html=True)

API_URL = "https://mtyzmxftd8.execute-api.ap-south-1.amazonaws.com/generate"

# ----- FORM -----
with st.form("resume_form"):

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>👤 Personal Information</div>", unsafe_allow_html=True)
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>💼 Professional Summary</div>", unsafe_allow_html=True)
    summary = st.text_area("Write a short professional summary")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>🛠 Skills</div>", unsafe_allow_html=True)
    skills = st.text_area("Comma-separated skills")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>🎓 Education</div>", unsafe_allow_html=True)
    education = st.text_area("Education details")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>📌 Projects</div>", unsafe_allow_html=True)
    projects = st.text_area("Each line: Title - Description - Tech Used")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>🏅 Certifications</div>", unsafe_allow_html=True)
    certifications = st.text_area("Certifications")
    st.markdown("</div>", unsafe_allow_html=True)

    submitted = st.form_submit_button("🚀 Generate Resume")

# ----- BACKEND CALL -----
if submitted:
    payload = {
        "name": name,
        "email": email,
        "phone": phone,
        "summary": summary,
        "skills": skills,
        "education": education,
        "projects": projects,
        "certifications": certifications,
    }

    with st.spinner("Generating resume… Please wait ⏳"):
        response = requests.post(API_URL, json=payload)
        data = response.json()

    resume_url = data.get("resume_url")

    if resume_url:
        st.success("🎉 Your resume is ready!")
        st.markdown(f"<a href='{resume_url}' target='_blank' class='download'>📄 Download Resume</a>", unsafe_allow_html=True)
    else:
        st.error("❌ Could not generate resume. Please try again.")
