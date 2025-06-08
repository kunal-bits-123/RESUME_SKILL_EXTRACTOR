import re
import fitz  # PyMuPDF
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_resume_data(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "experience": extract_experience(text)
    }

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    return "\n".join([page.get_text() for page in doc])

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text.strip()
    return "N/A"

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else "N/A"

def extract_phone(text):
    match = re.search(r'(\+?\d{1,3})?[\s\-\.]?\(?\d{3}\)?[\s\-\.]?\d{3}[\s\-\.]?\d{4}', text)
    return match.group(0) if match else "N/A"

def extract_experience(text):
    match = re.search(r'Experience\s*:?[\n ]*(\d+\s+years?.+)', text, re.IGNORECASE)
    return match.group(1).strip() if match else "N/A"

def extract_skills(text):
    # Attempt to locate "Skills" section more flexibly
    skills_match = re.search(r"Skills\s*[:\-]?\s*(.+)", text, re.IGNORECASE)
    
    if skills_match:
        skills_line = skills_match.group(1)

        # If it's a comma-separated line, split it
        if "," in skills_line:
            skills = [s.strip() for s in skills_line.split(",")]
        else:
            # Otherwise, split by whitespace or bullets
            skills = re.split(r"[•\n\-]", skills_line)
            skills = [s.strip() for s in skills if len(s.strip()) > 1]

        # Filter weird entries
        cleaned_skills = [s for s in skills if s.lower() not in ['address', 'email', 'phone']]
        return list(set(cleaned_skills))  # Remove duplicates
    else:
        return []
