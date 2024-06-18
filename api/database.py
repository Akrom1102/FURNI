from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

ENGINE = create_engine('postgresql://postgres:akrom_1102@localhost:5432/furni', echo=True)
Base = declarative_base()
session = sessionmaker()