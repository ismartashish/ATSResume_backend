from sklearn.metrics.pairwise import cosine_similarity
from services.embeddings import embed_pair
from services.skill_extractor import extract_skills

def match_resume(resume_text: str, job_text: str):
    # ✅ Proper semantic similarity
    res_vec, job_vec = embed_pair(resume_text, job_text)

    match_score = float(cosine_similarity([res_vec], [job_vec])[0][0])
    match_score = round(match_score * 100, 2)

    # ✅ Skill comparison
    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_text))

    missing_skills = list(job_skills - resume_skills)

    return match_score, missing_skills, list(job_skills)
