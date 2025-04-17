def extract_skills(text):
    skill_list = ['Python', 'Java', 'C++', 'Machine Learning', 'SQL', 'Docker']
    found = [skill for skill in skill_list if skill.lower() in text.lower()]
    return ', '.join(found) if found else "Not found"
