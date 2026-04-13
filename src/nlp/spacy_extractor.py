import spacy

nlp = spacy.load("en_core_web_sm")

# 🔥 STOPWORDS (remove junk)
STOP_SKILLS = {
    "experience", "knowledge", "skills", "ability",
    "understanding", "work", "team", "job",
    "responsibilities", "candidate"
}

def extract_skills(text):
    doc = nlp(text)

    skills = set()

    for token in doc:
        word = token.text.lower()

        # ✅ Only meaningful tokens
        if token.pos_ in ["NOUN", "PROPN"]:
            if word not in STOP_SKILLS and len(word) > 2:
                skills.add(word)

    return list(skills)