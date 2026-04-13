from sklearn.metrics.pairwise import cosine_similarity
from src.nlp.bert_model import model

def match_skills(resume_skills, jd_skills):
    matched, missing = [], []

    if not resume_skills or not jd_skills:
        return matched, jd_skills

    jd_emb = model.encode(jd_skills)
    res_emb = model.encode(resume_skills)

    for i, jd_skill in enumerate(jd_skills):
        sim = cosine_similarity([jd_emb[i]], res_emb)[0]

        if max(sim) > 0.7:
            matched.append(jd_skill)
        else:
            missing.append(jd_skill)

    return matched, missing