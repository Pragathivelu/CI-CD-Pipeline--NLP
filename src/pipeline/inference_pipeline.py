from src.preprocessing.clean import clean_text
from src.nlp.spacy_extractor import extract_skills
from src.features.skill_mapper import map_skills
from src.ontology.auto_update import auto_update
from src.nlp.bert_model import get_embedding
from src.matching.semantic_matcher import match_skills
from src.scoring.scorer import compute_score
from src.nlp.t5_model import generate_feedback

def run_pipeline(resume, jd):
    resume = clean_text(resume)
    jd = clean_text(jd)

    # 🔥 RAW SKILLS
    raw_res_skills = extract_skills(resume)
    raw_jd_skills = extract_skills(jd)

    # 🔥 AUTO LEARN
    auto_update(raw_jd_skills)

    # 🔥 MAPPED SKILLS
    res_skills = map_skills(raw_res_skills)
    jd_skills = map_skills(raw_jd_skills)

    print("Resume Skills:", res_skills)
    print("JD Skills:", jd_skills)

    matched, missing = match_skills(res_skills, jd_skills)

    res_emb = get_embedding(resume)
    jd_emb = get_embedding(jd)

    score = compute_score(res_emb, jd_emb, matched, jd_skills)

    feedback = generate_feedback(missing, round(score * 100, 2))

    return {
        "ATS Score": round(score * 100, 2),
        "Matched": matched,
        "Missing": missing,
        "Feedback": feedback
    }