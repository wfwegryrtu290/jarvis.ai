import asyncio

from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes

from config import OWNER_ID

from ai.brain import process

from memory.memory import save_message
from core.logger import logger


async def text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != OWNER_ID:

        await update.message.reply_text("⛔ Нямаш достъп.")
        return

    message = (update.message.text or "").strip()

    if not message:

        await update.message.reply_text("Изпрати текст.")
        return

    logger.info(f"USER: {message}")

    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING,
    )

    try:

        answer = await asyncio.to_thread(
            process,
            message,
        )

    except Exception as e:

        logger.exception(e)

        await update.message.reply_text(
            "❌ Възникна вътрешна грешка."
        )

        return

    if not answer:

        answer = "Нямам отговор."

    logger.info(f"JARVIS: {answer}")

    try:

        save_message(
            message,
            answer,
        )

    except Exception as e:

        logger.exception(e)

    await update.message.reply_text(answer)
