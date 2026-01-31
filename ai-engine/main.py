from fastapi import FastAPI, File, UploadFile, Form
from pydantic import BaseModel
import fitz  # PyMuPDF

# ... your other imports ...

app = FastAPI(title="ATS Resume AI")

@app.post("/resume/analyze")
async def analyze(
    resume: UploadFile = File(...), 
    job_description: str = Form(...)
):
    # 1. Read the PDF binary and extract text
    pdf_content = await resume.read()
    doc = fitz.open(stream=pdf_content, filetype="pdf")
    resume_text = ""
    for page in doc:
        resume_text += page.get_text()
    
    # 2. Run your existing logic using the extracted text
    resume_skills = extract_skills(resume_text)

    match_score, missing_skills, job_skills = match_resume(
        resume_text,
        job_description
    )

    resume_score = calculate_score(resume_skills, match_score)
    suggestions = improvement_suggestions(missing_skills, resume_score)

    ai_warnings = detect_ai_content(resume_text)
    repetitions = detect_repetition(resume_text)

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
