from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import fitz  # PyMuPDF
import re

app = FastAPI(title="ATS Resume AI")

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------
# SIMPLE ATS LOGIC FUNCTIONS
# ---------------------------

def extract_skills(text):
    common_skills = [
        # Programming Languages
        "python", "java", "c", "c++", "c#", "javascript", "typescript",
        "go", "rust", "kotlin", "swift", "php", "ruby",

        # Web Development
        "html", "css", "react", "next.js", "node", "express",
        "angular", "vue", "bootstrap", "tailwind", "redux",

        # Backend / Databases
        "mongodb", "mysql", "postgresql", "sqlite", "sql",
        "firebase", "redis", "oracle",

        # DevOps / Tools
        "docker", "kubernetes", "aws", "azure", "gcp",
        "jenkins", "github actions", "gitlab", "nginx",
        "linux", "bash", "shell scripting",

        # AI / ML / Data
        "machine learning", "deep learning", "tensorflow",
        "pytorch", "scikit-learn", "pandas", "numpy",
        "opencv", "nlp", "data analysis", "data science",

        # Mobile Development
        "android", "flutter", "react native", "ios",

        # CS Fundamentals
        "data structures", "algorithms", "oops",
        "operating systems", "computer networks",
        "dbms", "system design",

        # Testing
        "unit testing", "jest", "pytest", "selenium",

        # Other Tools
        "postman", "jira", "figma", "webpack", "vite"
    ]

    found = []
    text_lower = text.lower()

    for skill in common_skills:
        if skill in text_lower:
            found.append(skill.capitalize())

    return found


def match_resume(resume_text, job_description):
    resume_words = set(resume_text.lower().split())
    job_words = set(job_description.lower().split())

    common = resume_words.intersection(job_words)

    match_score = int((len(common) / max(len(job_words), 1)) * 100)

    missing_skills = list(job_words - resume_words)[:5]

    return match_score, missing_skills, list(job_words)[:10]


def calculate_score(resume_skills, match_score):
    base = match_score
    bonus = len(resume_skills) * 2
    return min(base + bonus, 100)


def improvement_suggestions(missing_skills, score):
    suggestions = []

    if missing_skills:
        suggestions.append("Add missing technical skills to your projects.")

    if score < 60:
        suggestions.append("Improve keyword alignment with job description.")

    suggestions.append("Use measurable achievements in experience section.")

    return suggestions


def detect_ai_content(text):
    warnings = []
    if "hardworking individual" in text.lower():
        warnings.append("Generic phrase detected: 'hardworking individual'")
    return warnings


def detect_repetition(text):
    words = re.findall(r'\b\w+\b', text.lower())
    repetition_data = []

    for word in set(words):
        count = words.count(word)
        if count > 8 and len(word) > 4:
            repetition_data.append({"word": word, "count": count})

    return repetition_data


def premium_ats_checks(resume_skills, job_skills, missing_skills, ai_warnings, repetitions):
    keyword_coverage = int(
        (len(resume_skills) / max(len(job_skills), 1)) * 100
    )

    ai_risk = "High" if ai_warnings else "Low"

    repetition_penalty = len(repetitions) * 2

    section_score = 80 - repetition_penalty

    return {
        "keywordCoverage": keyword_coverage,
        "aiRisk": ai_risk,
        "repetitionPenalty": repetition_penalty,
        "sectionScore": section_score
    }

# ---------------------------
# MAIN ENDPOINT
# ---------------------------

@app.post("/resume/analyze")
async def analyze(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    try:
        if resume.content_type != "application/pdf":
            raise HTTPException(status_code=400, detail="Only PDF files allowed.")

        pdf_content = await resume.read()

        if not pdf_content:
            raise HTTPException(status_code=400, detail="Empty file uploaded.")

        doc = fitz.open(stream=pdf_content, filetype="pdf")
        resume_text = ""

        for page in doc:
            resume_text += page.get_text()

        doc.close()

        if not resume_text.strip():
            raise HTTPException(status_code=400, detail="Could not extract text.")

        # ATS Logic
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
            "resumeText": resume_text,
            "premiumATS": premium
        }

    except Exception as e:
        import traceback
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
def health():
    return {"status": "ATS Backend Running"}
