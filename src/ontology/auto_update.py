import json
import os

BASE = "data/ontology"

def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def auto_update(jd_skills):
    skills = load_json(f"{BASE}/skills.json")
    new_skills = load_json(f"{BASE}/new_skills.json")

    known = set(skills.keys())

    for skill in jd_skills:
        if skill not in known:
            new_skills[skill] = [skill]

    save_json(f"{BASE}/new_skills.json", new_skills)