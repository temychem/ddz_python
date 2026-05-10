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


def process_excel(file_path, output_path):
    df = pd.read_excel(file_path)

    for col in df.columns:

        if col in ["Fullname", "Номер по списку"]:
            continue

        if "(5-балльная)" in col:
            continue

        max_score = extract_max_score(col)
        if not max_score:
            continue

        new_col = f"{col} (5-балльная)"

        if new_col in df.columns:
            continue

        def temp(x):
            return convert_to_scale(x, max_score)

        df[new_col] = (
            df[col]
            .apply(clean_score)
            .apply(temp)
        )

        df.to_excel(output_path, index=False)

