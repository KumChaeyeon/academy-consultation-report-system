import pandas as pd


def clean_data(df):

    df = df.copy()

    df["상담일자"] = pd.to_datetime(df["상담일자"])

    df["등록여부"] = df["등록여부"].fillna("미전환")

    df["등록여부"] = df["등록여부"].apply(
        lambda x: 1 if x == "전환" else 0
    )

    df = df.drop(columns=["이름"])

    return df
