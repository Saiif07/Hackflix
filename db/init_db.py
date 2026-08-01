"""
Initialize database (create tables)
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base


def init_db(database_url: str = "sqlite:///hackflix.db"):
    engine = create_engine(database_url, connect_args={"check_same_thread": False} if database_url.startswith("sqlite") else {})
    Base.metadata.create_all(engine)
    return engine
