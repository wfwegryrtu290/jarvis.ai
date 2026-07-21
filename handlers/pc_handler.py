from telegram import Update
from telegram.ext import ContextTypes

from config import OWNER_ID
from commands import get_pc_info


async def pc(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != OWNER_ID:
        return

    await update.message.reply_text(
        get_pc_info()
    )