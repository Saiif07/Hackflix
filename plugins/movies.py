"""
Movie-related commands: movie_update toggle, top
"""
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from db.init_db import init_db
from db.models import Setting
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///hackflix.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {})
Session = sessionmaker(bind=engine)


def cmd_movie_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    session = Session()
    # Toggle setting
    s = session.query(Setting).filter_by(chat_id=chat_id, key='movie_update').first()
    if s and s.value == '1':
        s.value = '0'
        session.add(s)
        session.commit()
        update.message.reply_text("Movie update notifications disabled for this chat.")
    else:
        if not s:
            s = Setting(chat_id=chat_id, key='movie_update', value='1')
        else:
            s.value = '1'
        session.add(s)
        session.commit()
        update.message.reply_text("Movie update notifications enabled for this chat.")
    session.close()


def cmd_top(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Stub: return sample trending titles
    sample = [
        "1. Example Movie A",
        "2. Example Movie B",
        "3. Example Movie C",
    ]
    update.message.reply_text("Trending:\n" + "\n".join(sample))


def register(app):
    app.add_handler(CommandHandler("movie_update", cmd_movie_update))
    app.add_handler(CommandHandler("top", cmd_top))
