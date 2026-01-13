from sklearn.metrics.pairwise import cosine_similarity
from services.embeddings import embed
from services.skill_extractor import extract_skills

def match_resume(resume_text, job_text):
    res_vec = embed(resume_text)
    job_vec = embed(job_text)

    match_score = float(cosine_similarity([res_vec], [job_vec])[0][0])
    match_score = round(match_score * 100, 2)

    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_text))

    missing_skills = list(job_skills - resume_skills)

    return match_score, missing_skills, list(job_skills)
