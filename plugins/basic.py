"""
Basic commands plugin: start, help, id, info
"""
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from db.init_db import init_db


def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text(
        "Welcome to Hackflix! Use /help to see available commands."
    )


def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Available commands:\n"
        "/start - Start bot\n"
        "/help - Show this message\n"
        "/id - Get your Telegram ID\n"
        "/info - Get bot info"
    )
    update.message.reply_text(text)


def cmd_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    update.message.reply_text(f"Your Telegram ID: {uid}")


def cmd_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text("Hackflix — group streaming & file hub. Use /help for commands.")


def register(app):
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("help", cmd_help))
    app.add_handler(CommandHandler("id", cmd_id))
    app.add_handler(CommandHandler("info", cmd_info))
