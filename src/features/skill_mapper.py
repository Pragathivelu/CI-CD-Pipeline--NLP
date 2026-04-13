import json

def load_ontology():
    with open("data/ontology/skills.json") as f:
        return json.load(f)

def map_skills(skills):
    ontology = load_ontology()
    mapped = []

    for skill in skills:
        found = False
        for key, values in ontology.items():
            if skill in values:
                mapped.append(key)
                found = True
                break

        # 🔥 KEEP NEW SKILLS ALSO
        if not found:
            mapped.append(skill)

    return list(set(mapped))