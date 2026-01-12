def calculate_score(skills, match_score):
    skill_score = min(len(skills) * 5, 40)
    match_component = float(match_score) * 0.6
    return int(skill_score + match_component)
 