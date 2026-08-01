# Hackflix

Hackflix — Your group streaming & file hub.

Tagline: Stream. Share. Secure.

Short description
Hackflix is a Telegram bot for group streaming, file management, and premium membership control. Supports double DB mode, advanced verification, AI spelling correction, big-file indexing, auto movie updates, and more — built for group admins who want fast, secure, and automated media sharing.

Key features
- Double DB support
- Stream Mode Toggle
- 3-step Verification system
- Group owners can manage settings via bot PM
- Spell check toggle (group only)
- Auto Movie Info Updates
- File indexing > 2GB, PreDVD & CamRip auto-deletion
- Verified user counter & verified DB save
- Premium membership management
- Fast broadcasts (users & groups)
- Forward restriction, file protection, auto file send
- Logs, stats & admin tools

Quick start (generic)
1. Clone the repo:
   git clone https://github.com/<your-org>/hackflix.git
   cd hackflix

2. Create a virtual env and install requirements (example for Python):
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

3. Environment variables (example):
   - BOT_TOKEN=your_telegram_bot_token
   - DATABASE_URL=postgres://user:pass@host:port/dbname  (or your DB connection)
   - REDIS_URL=redis://host:port (optional)
   - ADMIN_IDS=123456789 (comma-separated)

4. Run the bot:
   python bot.py

Notes
- Backup your database before switching to double DB mode.
- Group owners can adjust group settings via private message with the bot.
- Reset All Group Settings is owner-only — use carefully.

Need platform-specific setup (Docker, PM2, systemd)? Ask and I'll add deployment instructions or a Dockerfile.