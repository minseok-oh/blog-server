import pymysql
from dotenv import load_dotenv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()


class DbConfig:
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")

    def get_connection_string(self):
        return f"mysql+mysqldb://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


db_config = DbConfig()
pymysql.install_as_MySQLdb()

SQLALCHEMY_DATABASE_URL = db_config.get_connection_string()
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
