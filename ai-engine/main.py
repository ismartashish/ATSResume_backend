from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import fitz  # PyMuPDF

app = FastAPI(title="ATS Resume AI")

# 🔥 CORS (important for React frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/resume/analyze")
async def analyze(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    try:
        # ✅ Validate file type
        if resume.content_type != "application/pdf":
            raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

        # ✅ Read PDF
        pdf_content = await resume.read()

        if len(pdf_content) == 0:
            raise HTTPException(status_code=400, detail="Uploaded file is empty.")

        # ✅ Extract text safely
        doc = fitz.open(stream=pdf_content, filetype="pdf")
        resume_text = ""

        for page in doc:
            resume_text += page.get_text()

        doc.close()  # 🔥 Always close document

        if not resume_text.strip():
            raise HTTPException(status_code=400, detail="Could not extract text from PDF.")

        # -----------------------------------
        # 🔎 YOUR ATS LOGIC
        # -----------------------------------

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

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
