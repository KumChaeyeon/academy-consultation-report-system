import os
import pandas as pd


def generate_excel_report(result, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        summary_df = pd.DataFrame({
            "항목": ["총 상담 건수", "등록 전환 건수", "등록 전환율"],
            "값": [
                result["total_count"],
                result["conversion_count"],
                f'{result["conversion_rate"]}%'
            ]
        })

        summary_df.to_excel(writer, sheet_name="요약", index=False)
        result["grade_summary"].to_excel(writer, sheet_name="학년별 상담", index=False)
        result["school_summary"].head(10).to_excel(writer, sheet_name="학교별 TOP10", index=False)
        result["monthly_summary"].to_excel(writer, sheet_name="월별 상담", index=False)

        result["grade_conversion"].to_excel(writer, sheet_name="학년별 전환율", index=False)
        result["school_conversion"].head(10).to_excel(writer, sheet_name="학교별 전환율 TOP10", index=False)
        result["monthly_conversion"].to_excel(writer, sheet_name="월별 전환율", index=False)
