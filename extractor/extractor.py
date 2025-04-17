import re
import spacy
from .skills import extract_skills

nlp = spacy.load("en_core_web_sm")

def extract_info(text):
    info = {}

    # Email
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    info['email'] = email_match.group(0) if email_match else "Not found"

    # Phone
    phone_match = re.search(r'\+?\d[\d -]{8,12}\d', text)
    info['phone'] = phone_match.group(0) if phone_match else "Not found"

    # Name
    doc = nlp(text)
    names = [ent.text for ent in doc.ents if ent.label_ == 'PERSON']
    info['name'] = names[0] if names else "Not found"

    # Skills
    info['skills'] = extract_skills(text)

    return info
