def premium_ats_checks(
    resume_skills,
    job_skills,
    missing_skills,
    ai_warnings,
    repetitions
):
    total_keywords = len(job_skills) if job_skills else 1
    matched_keywords = total_keywords - len(missing_skills)

    keyword_coverage = round(
        (matched_keywords / total_keywords) * 100, 2
    )

    ai_risk = (
        "High" if len(ai_warnings) >= 4 else
        "Medium" if len(ai_warnings) >= 2 else
        "Low"
    )

    repetition_penalty = sum(
        max(0, r["count"] - 3) for r in repetitions
    )

    section_score = 100
    if missing_skills:
        section_score -= 15
    if ai_risk == "High":
        section_score -= 20

    return {
        "keywordCoverage": keyword_coverage,
        "aiRisk": ai_risk,
        "repetitionPenalty": repetition_penalty,
        "sectionScore": max(section_score, 50),
        "atsSafe": True
    }
