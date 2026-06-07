from data_loading import load_excel_data
from data_cleaning import clean_data

from database import get_engine
from database_manager import create_schemas, save_to_staging, create_core_table

from db_analysis import analyze_data_from_db
from report_generator import generate_excel_report


file_path = "data/raw/consultation.xlsx"
output_path = "reports/monthly_consultation_report_db.xlsx"

df = load_excel_data(file_path)
df = clean_data(df)

engine = get_engine()

create_schemas(engine)
save_to_staging(df, engine)
create_core_table(df, engine)

result = analyze_data_from_db(engine)

generate_excel_report(result, output_path)

print("월간 상담 리포트 생성 완료")
print(output_path)
