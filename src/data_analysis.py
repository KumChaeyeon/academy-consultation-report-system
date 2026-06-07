def analyze_data(df):
    total_count = len(df)

    conversion_count = df["등록여부"].sum()

    conversion_rate = round((conversion_count / total_count) * 100, 2)

    grade_summary = df.groupby("학년").size().reset_index(name="상담건수")

    school_summary = (
        df.groupby("학교")
        .size()
        .reset_index(name="상담건수")
        .sort_values(by="상담건수", ascending=False)
    )

    monthly_summary = (
        df.groupby(df["상담일자"].dt.to_period("M"))
        .size()
        .reset_index(name="상담건수")
    )

    monthly_summary["상담일자"] = monthly_summary["상담일자"].astype(str)

    result = {
        "total_count": total_count,
        "conversion_count": conversion_count,
        "conversion_rate": conversion_rate,
        "grade_summary": grade_summary,
        "school_summary": school_summary,
        "monthly_summary": monthly_summary
    }

    return result
