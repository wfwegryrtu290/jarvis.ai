from telegram import Update
from telegram.ext import ContextTypes

from config import OWNER_ID
from workspace.scanner import scan


async def scan_workspace(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != OWNER_ID:
        return

    await update.message.reply_text(
        "🔍 Сканирам workspace..."
    )

    total = scan(r"C:\Users\rusev")

    await update.message.reply_text(
        f"✅ Сканирането приключи.\n\n"
        f"Индексирани файлове: {total}"
    )