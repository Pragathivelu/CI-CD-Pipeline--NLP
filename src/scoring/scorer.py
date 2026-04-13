from sklearn.metrics.pairwise import cosine_similarity

def compute_score(res_emb, jd_emb, matched, jd_skills):
    semantic = cosine_similarity([res_emb], [jd_emb])[0][0]
    skill = len(matched) / (len(jd_skills) + 1e-5)
    return 0.6 * semantic + 0.4 * skill