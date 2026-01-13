from sklearn.metrics.pairwise import cosine_similarity
from services.embeddings import embed
from services.skill_extractor import extract_skills


def match_resume(resume_text, job_text):
    # 🔹 Embed BOTH texts together (TF-IDF requirement)
    vectors = embed([resume_text, job_text])

    res_vec = vectors[0]
    job_vec = vectors[1]

    # 🔹 Cosine similarity
    match_score = cosine_similarity([res_vec], [job_vec])[0][0]
    match_score = round(float(match_score) * 100, 2)

    # 🔹 Skill extraction
    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_text))

    # 🔹 Missing skills (real ATS logic)
    missing_skills = list(job_skills - resume_skills)

    return match_score, missing_skills, list(job_skills)
