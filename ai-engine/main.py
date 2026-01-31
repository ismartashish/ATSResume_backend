from fastapi import FastAPI
from pydantic import BaseModel

from services.matcher import match_resume
from services.skill_extractor import extract_skills
from services.resume_score import calculate_score
from services.improvement import improvement_suggestions
from services.ai_detector import detect_ai_content
from services.repetition_detector import detect_repetition
from services.premium_ats import premium_ats_checks

app = FastAPI(title="ATS Resume AI")

class AnalyzeRequest(BaseModel):
    resume_text: str
    job_description: str

@app.get("/")
def root():
    return {"status": "ATS Resume AI running"}

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/resume/analyze")
def analyze(data: AnalyzeRequest):
    resume_skills = extract_skills(data.resume_text)

    match_score, missing_skills, job_skills = match_resume(
        data.resume_text,
        data.job_description
    )

    resume_score = calculate_score(resume_skills, match_score)
    suggestions = improvement_suggestions(missing_skills, resume_score)

    ai_warnings = detect_ai_content(data.resume_text)
    repetitions = detect_repetition(data.resume_text)

    premium = premium_ats_checks(
        resume_skills,
        job_skills,
        missing_skills,
        ai_warnings,
        repetitions
    )

    return {
        "resumeScore": resume_score,
        "matchScore": match_score,
        "resumeSkills": resume_skills,
        "jobSkills": job_skills,
        "missingSkills": missing_skills,
        "suggestions": suggestions,
        "aiWarnings": ai_warnings,
        "repetitions": repetitions,
        "premiumATS": premium
    }
