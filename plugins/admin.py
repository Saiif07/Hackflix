"""
Admin commands: ban, unban, broadcast (simple implementations)
"""
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from config import settings


def is_admin(user_id: int):
    return user_id in settings.ADMIN_IDS


def cmd_ban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if not is_admin(user.id):
        update.message.reply_text("You are not authorized to use this command.")
        return
    if not context.args:
        update.message.reply_text("Usage: /ban <user_id>")
        return
    try:
        target = int(context.args[0])
        # Store ban in DB (stub)
        update.message.reply_text(f"User {target} has been banned (stub).")
    except ValueError:
        update.message.reply_text("Invalid user id.")


def cmd_unban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if not is_admin(user.id):
        update.message.reply_text("You are not authorized to use this command.")
        return
    if not context.args:
        update.message.reply_text("Usage: /unban <user_id>")
        return
    try:
        target = int(context.args[0])
        update.message.reply_text(f"User {target} has been unbanned (stub).")
    except ValueError:
        update.message.reply_text("Invalid user id.")


def cmd_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if not is_admin(user.id):
        update.message.reply_text("You are not authorized to use this command.")
        return
    if not context.args:
        update.message.reply_text("Usage: /broadcast <message>")
        return
    message = " ".join(context.args)
    # Broadcast logic stub: in real app, iterate DB users and send
    update.message.reply_text("Broadcast sent to users (stub).")


def register(app):
    app.add_handler(CommandHandler("ban", cmd_ban))
    app.add_handler(CommandHandler("unban", cmd_unban))
    app.add_handler(CommandHandler("broadcast", cmd_broadcast))
