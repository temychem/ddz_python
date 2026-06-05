import pandas as pd
from excel.convert import process_excel


def test_process_excel(tmp_path):

    input_file = tmp_path / "input.xlsx"
    output_file = tmp_path / "output.xlsx"

    df = pd.DataFrame({
        "Fullname": ["2025-4-03-gol"],
        "Номер по списку": [3],
        "pz1 + pz2 10 вопросов": [8]
    })

    df.to_excel(input_file, index=False)

    process_excel(input_file, output_file)

    result_df = pd.read_excel(output_file)

    assert "pz1 + pz2 10 вопросов (5-балльная)" in result_df.columns

    assert result_df.loc[0, "pz1 + pz2 10 вопросов (5-балльная)"] == 4