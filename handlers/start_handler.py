from telegram import Update
from telegram.ext import ContextTypes

from config import OWNER_ID


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != OWNER_ID:
        return

    await update.message.reply_text(
        "🤖 Jarvis е онлайн!"
    )