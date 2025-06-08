import re
import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

def extract_email(text):
    m = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return m.group(0) if m else ""

def extract_phone(text):
    m = re.search(r'\+?\d[\d\s\-]{8,15}', text)
    return m.group(0) if m else ""

def extract_experience(text):
    lines = text.split("\n")
    return [ln.strip() for ln in lines if any(w in ln.lower() for w in ["experience","responsible","worked","develop"])][:10]

def extract_skills(text):
    doc = nlp(text)
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    # collect noun chunks as candidate skills
    chunks = list({chunk.text.strip() for chunk in doc.noun_chunks if len(chunk.text.split()) <= 3})
    matcher.add("SKILL", [nlp.make_doc(chunk) for chunk in chunks])
    matches = matcher(doc)
    return list({doc[start:end].text for _, start, end in matches})
