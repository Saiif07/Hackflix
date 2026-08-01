#!/bin/bash
# Simple helper to run the bot
if [ -f ".env" ]; then
  export $(grep -v '^#' .env | xargs)
fi
python bot.py
