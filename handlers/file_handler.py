from telegram import Update
from telegram.ext import ContextTypes

from config import OWNER_ID
from file_reader import read_file


async def file_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != OWNER_ID:
        return

    file = await update.message.document.get_file()

    filename = update.message.document.file_name

    path = "files_" + filename

    await file.download_to_drive(path)

    text = read_file(path)

    await update.message.reply_text(
        "📄 Файлът е прочетен!\n\n" + text[:3000]
    )