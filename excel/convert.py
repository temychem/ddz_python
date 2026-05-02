def convert_to_scale(score, max_score):
    if score is None:
        return None

    percent = score / max_score

    if percent >= 0.9:
        return 5
    elif percent >= 0.7:
        return 4
    elif percent >= 0.5:
        return 3
    elif percent >= 0.3:
        return 2
    elif percent >= 0.1:
        return 1
    else:
        return 0