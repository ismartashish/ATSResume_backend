def ats_breakdown(resume_skills, missing_role):
    keyword = max(0, 100 - len(missing_role) * 10)

    return {
        "keywordMatch": keyword,
        "formatting": 85,
        "atsCompatibility": int((keyword + 85) / 2)
    }
