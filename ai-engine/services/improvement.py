def improvement_suggestions(missing_skills, resume_score):
    suggestions = []

    for skill in missing_skills:
        suggestions.append(
            f"Add a project or work experience demonstrating {skill}"
        )

    suggestions.extend([
        "Use action verbs like built, optimized, deployed",
        "Add metrics (e.g. improved performance by 30%)",
        "Mention tools used clearly in each project"
    ])

    return suggestions
