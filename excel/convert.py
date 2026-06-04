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


def convert_to_scale(
    score,
    max_score,
    grade_5=0.9,
    grade_4=0.7,
    grade_3=0.5,
    grade_2=0.3,
    grade_1=0.1
):

    if score is None:
        return None

    percent = score / max_score

    if percent >= grade_5:
        return 5

    elif percent >= grade_4:
        return 4

    elif percent >= grade_3:
        return 3

    elif percent >= grade_2:
        return 2

    elif percent >= grade_1:
        return 1

    return 0


def process_excel(
    file_path,
    output_path,
    grade_5=0.9,
    grade_4=0.7,
    grade_3=0.5,
    grade_2=0.3,
    grade_1=0.1
):

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

        def temp(x):
            return convert_to_scale(x, max_score)


        if new_col in df.columns:
            continue

        df[new_col] = (
            df[col]
            .apply(clean_score)
            .apply(temp)
            )

    df.to_excel(output_path, index=False)
