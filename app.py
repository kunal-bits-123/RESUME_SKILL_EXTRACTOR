import streamlit as st
from extractor import extract_resume_data
from storage import save_result, load_all_results
import os

st.set_page_config(page_title="Resume Skill Extractor", layout="centered")
st.title("Resume Skill Extractor (with spaCy)")

st.markdown("Upload one or more resume PDFs. The app will extract structured data like name, email, phone, skills, and work experience.")

uploaded_files = st.file_uploader("Upload Resume PDFs", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        # Save temporarily just to read it
        temp_path = f"temp_{uploaded_file.name}"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.read())

        # Extract and store structured data
        data = extract_resume_data(temp_path)
        save_result(data)

        # Delete the temporary file
        os.remove(temp_path)

        # Display parsed data
        st.success(f"Parsed {uploaded_file.name} successfully!")
        st.markdown("### Parsed Resume Data")
        st.markdown(f"#### Personal Info")
        st.markdown(f"- **Name**: {data.get('name', 'N/A')}")
        st.markdown(f"- **Email**: {data.get('email', 'N/A')}")
        st.markdown(f"- **Phone**: {data.get('phone', 'N/A')}")

        st.markdown("#### Skills")
        for skill in data.get("skills", []):
            st.markdown(f"- {skill}")

        st.markdown("#### 💼 Work Experience")
        st.markdown(f"{data.get('experience', 'N/A')}")

# Skill-based filtering
st.markdown("---")
st.markdown("## Filter Resumes by Skill (Stored Resumes)")
skill = st.text_input("Enter a skill to filter stored resumes")

if skill:
    results = [
        r for r in load_all_results()
        if skill.lower() in [s.lower() for s in r.get("skills", [])]
    ]
    st.write(f"Found **{len(results)}** resume(s) with skill: `{skill}`")

    for i, r in enumerate(results):
        st.markdown(f"### 📄 Match {i + 1}")
        st.markdown(f"**Name**: {r.get('name')}")
        st.markdown(f"**Email**: {r.get('email')}")
        st.markdown(f"**Phone**: {r.get('phone')}")
        st.markdown(f"**Skills**: {', '.join(r.get('skills', []))}")
        st.markdown(f"**Experience**: {r.get('experience')}")
