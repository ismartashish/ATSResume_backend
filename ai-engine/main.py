from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware



from services.matcher import match_resume
from services.skill_extractor import extract_skills
from services.resume_score import calculate_score
from services.improvement import improvement_suggestions
from services.ai_detector import detect_ai_content
from services.repetition_detector import detect_repetition
from services.premium_ats import premium_ats_checks

app = FastAPI(title="ATS Resume AI")

# ✅ CORS (important for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# HEALTH CHECK
# -------------------------
@app.get("/health")
def health():
    return {"status": "ok"}

# -------------------------
# MAIN ANALYSIS ENDPOINT
# -------------------------
@app.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    jobDescription: str = Form(...)
):
    # 1. Extract resume text
    resume_text = extract_text_from_pdf(resume.file)

    # 2. Skills
    resume_skills = extract_skills(resume_text)

    # 3. Match score
    match_score, missing_skills, job_skills = match_resume(
        resume_text,
        jobDescription
    )

    # 4. Resume score
    resume_score = calculate_score(resume_skills, match_score)

    # 5. Suggestions
    suggestions = improvement_suggestions(missing_skills, resume_score)

    # 6. AI warnings
    ai_warnings = detect_ai_content(resume_text)

    # 7. Repetitions
    repetitions = detect_repetition(resume_text)

    # 8. Premium ATS
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
        "resumeText": resume_text,
        "premiumATS": premium
    }
