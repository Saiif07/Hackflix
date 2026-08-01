"""
Simple SQLAlchemy models for Hackflix
"""
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, index=True, nullable=False)
    username = Column(String(255))
    is_verified = Column(Boolean, default=False)
    is_banned = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())

class FileRecord(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    file_id = Column(String(255), index=True)
    title = Column(String(512))
    size = Column(Integer)
    uploaded_by = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())

class Setting(Base):
    __tablename__ = 'settings'
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, index=True)
    key = Column(String(128))
    value = Column(Text)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
