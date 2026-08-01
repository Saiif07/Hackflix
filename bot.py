"""
Hackflix - Telegram bot main entrypoint
"""
import os
import logging
from pathlib import Path
from importlib import import_module
import glob

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

from config import settings
from utils.logger import setup_logging
from db.init_db import init_db

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

PLUGINS_DIR = Path(__file__).parent / "plugins"

async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Unknown command. Use /help to see available commands.")

def load_plugins(application):
    """Dynamically import all plugin modules and call their register(app) function."""
    plugin_files = glob.glob(str(PLUGINS_DIR / "*.py"))
    for p in plugin_files:
        name = Path(p).stem
        if name.startswith("__"):
            continue
        module_path = f"plugins.{name}"
        try:
            module = import_module(module_path)
            if hasattr(module, "register"):
                module.register(application)
                logger.info(f"Loaded plugin: {module_path}")
            else:
                logger.warning(f"Plugin {module_path} has no register(app) function")
        except Exception as e:
            logger.exception(f"Error loading plugin {module_path}: {e}")

async def main():
    # Ensure DB exists
    init_db(settings.DATABASE_URL)

    # Build the bot application
    app = ApplicationBuilder().token(settings.BOT_TOKEN).build()

    # Load plugins (they should register handlers on the application)
    load_plugins(app)

    # Fallback for unknown commands
    app.add_handler(MessageHandler(filters.COMMAND, unknown_command))

    logger.info("Starting Hackflix bot...")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await app.idle()

if __name__ == '__main__':
    import asyncio
    load_dotenv()
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
