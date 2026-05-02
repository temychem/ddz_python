import re
import pandas as pd

def extract_max_score(column_name):
    match = re.search(r'(\d+)\s*вопрос', column_name.lower())
    if match:
        return int(match.group(1))
    else:
        return None

def clean_score(value):
    if value == "-" or pd.isna(value):
        return None
    try:
        return float(value)
    except:
        return None


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