import pandas as pd


def analyze_data_from_db(engine):
    total_count_query = """
        SELECT COUNT(*) AS total_count
        FROM core.consultation;
    """

    conversion_query = """
        SELECT SUM("등록여부") AS conversion_count
        FROM core.consultation;
    """

    grade_query = """
        SELECT "학년", COUNT(*) AS "상담건수"
        FROM core.consultation
        GROUP BY "학년"
        ORDER BY "상담건수" DESC;
    """

    school_query = """
        SELECT "학교", COUNT(*) AS "상담건수"
        FROM core.consultation
        WHERE "학교" IS NOT NULL
        GROUP BY "학교"
        ORDER BY "상담건수" DESC;
    """

    monthly_query = """
        SELECT "상담월", COUNT(*) AS "상담건수"
        FROM core.consultation
        GROUP BY "상담월"
        ORDER BY "상담월";
    """

    grade_conversion_query = """
        SELECT
            "학년",
            COUNT(*) AS "상담건수",
            SUM("등록여부") AS "등록건수",
            ROUND(SUM("등록여부")::numeric / COUNT(*) * 100, 2) AS "전환율"
        FROM core.consultation
        GROUP BY "학년"
        ORDER BY "전환율" DESC;
    """

    school_conversion_query = """
        SELECT
            "학교",
            COUNT(*) AS "상담건수",
            SUM("등록여부") AS "등록건수",
            ROUND(SUM("등록여부")::numeric / COUNT(*) * 100, 2) AS "전환율"
        FROM core.consultation
        WHERE "학교" IS NOT NULL
        GROUP BY "학교"
        HAVING COUNT(*) >= 3
        ORDER BY "전환율" DESC;
    """

    monthly_conversion_query = """
        SELECT
            "상담월",
            COUNT(*) AS "상담건수",
            SUM("등록여부") AS "등록건수",
            ROUND(SUM("등록여부")::numeric / COUNT(*) * 100, 2) AS "전환율"
        FROM core.consultation
        GROUP BY "상담월"
        ORDER BY "상담월";
    """

    total_count = pd.read_sql(total_count_query, engine).iloc[0]["total_count"]
    conversion_count = pd.read_sql(conversion_query, engine).iloc[0]["conversion_count"]

    conversion_rate = round((conversion_count / total_count) * 100, 2)

    grade_summary = pd.read_sql(grade_query, engine)
    school_summary = pd.read_sql(school_query, engine)
    monthly_summary = pd.read_sql(monthly_query, engine)

    grade_conversion = pd.read_sql(grade_conversion_query, engine)
    school_conversion = pd.read_sql(school_conversion_query, engine)
    monthly_conversion = pd.read_sql(monthly_conversion_query, engine)

    result = {
        "total_count": total_count,
        "conversion_count": conversion_count,
        "conversion_rate": conversion_rate,
        "grade_summary": grade_summary,
        "school_summary": school_summary,
        "monthly_summary": monthly_summary,
        "grade_conversion": grade_conversion,
        "school_conversion": school_conversion,
        "monthly_conversion": monthly_conversion
    }

    return result
