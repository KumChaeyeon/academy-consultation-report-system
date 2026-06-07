import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()


def get_engine():

    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")

    engine = create_engine(
        f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
    )

    return engine
