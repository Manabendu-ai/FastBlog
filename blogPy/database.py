from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONNECTION_URL = "sqlite.///./blogdb.db"
CONNECTION_ARGS = {
    "check_same_thread" : False
}

engine = create_engine(
    CONNECTION_URL,
    connect_args=CONNECTION_ARGS
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

Base = declarative_base()