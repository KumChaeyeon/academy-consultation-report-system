import pandas as pd


def load_excel_data(file_path):
    df = pd.read_excel(file_path, header=None)

    df = df.iloc[1:, :9]

    df.columns = [
        "번호",
        "상담유형",
        "상담일자",
        "학년",
        "이름",
        "학교",
        "담당자",
        "상담내용",
        "등록여부"
    ]

    df = df[[
        "상담일자",
        "학년",
        "이름",
        "학교",
        "상담내용",
        "등록여부"
    ]]

    return df
