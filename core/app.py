from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import TOKEN

from handlers.start_handler import start
from handlers.pc_handler import pc
from handlers.scan_handler import scan_workspace
from handlers.file_handler import file_handler
from handlers.text_handler import text_message

from core.logger import logger
from core.startup import startup


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):

    logger.exception(context.error)

    print("\n========== ERROR ==========")
    print(context.error)
    print("===========================\n")

    try:

        if isinstance(update, Update) and update.effective_message:

            await update.effective_message.reply_text(
                "❌ Възникна вътрешна грешка."
            )

    except Exception:
        pass


def create_app():

    logger.info("Startup...")

    startup()

    app = (
        Application.builder()
        .token(TOKEN)
        .build()
    )

    app.add_error_handler(error_handler)

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("pc", pc))
    app.add_handler(CommandHandler("scan", scan_workspace))

    # Files
    app.add_handler(
        MessageHandler(
            filters.Document.ALL,
            file_handler,
        )
    )

    # Photos
    app.add_handler(
        MessageHandler(
            filters.PHOTO,
            file_handler,
        )
    )

    # Text
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            text_message,
        )
    )

    logger.info("Telegram application created.")

    return app
