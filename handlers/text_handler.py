import asyncio

from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ChatAction

from config import OWNER_ID
from ai.brain import process
from memory.memory import save_message


async def text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text("Нямаш достъп.")
        return

    message = update.message.text

    print(f"👤 {update.effective_user.first_name}: {message}")

    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING
    )

    answer = await asyncio.to_thread(process, message)

    print(f"🤖 Jarvis: {answer}")

    save_message(message, answer)

    await update.message.reply_text(answer)