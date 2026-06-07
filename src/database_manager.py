import pandas as pd
from sqlalchemy import text


def create_schemas(engine):
    with engine.begin() as conn:
        conn.execute(text(
            "CREATE SCHEMA IF NOT EXISTS staging"
        ))

        conn.execute(text(
            "CREATE SCHEMA IF NOT EXISTS core"
        ))

    print("스키마 생성 완료")

def save_to_staging(df, engine):
    df.to_sql(
        name="consultation",
        con=engine,
        schema="staging",
        if_exists="replace",
        index=False
    )

    print("staging 저장 완료")

def create_core_table(df, engine):

    core_df = df.copy()

    core_df["상담월"] = core_df["상담일자"].dt.strftime("%Y-%m")
    core_df["연도"] = core_df["상담일자"].dt.year
    core_df["월"] = core_df["상담일자"].dt.month

    core_df.to_sql(
        name="consultation",
        con=engine,
        schema="core",
        if_exists="replace",
        index=False
    )

    print("core 저장 완료")
