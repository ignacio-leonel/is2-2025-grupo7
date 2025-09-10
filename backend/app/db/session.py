from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.app.db.base import base

DATABASE_URL = "sqlite:///./test.db"  # Base SQLite local

engine = create_engine(DATABASE_URL, echo=True)  # echo=True = muestra SQL en consola
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    base.metadata.create_all(bind=engine)