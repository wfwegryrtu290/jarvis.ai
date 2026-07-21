from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import TOKEN

from handlers.start_handler import start
from handlers.pc_handler import pc
from handlers.scan_handler import scan_workspace
from handlers.file_handler import file_handler
from handlers.text_handler import text_message

from core.startup import startup


def create_app():

    startup()

    app = Application.builder().token(TOKEN).build()

    async def error_handler(update, context):

        print("\n========== ERROR ==========")
        print(context.error)
        print("===========================\n")

    app.add_error_handler(error_handler)

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("pc", pc))
    app.add_handler(CommandHandler("scan", scan_workspace))

    app.add_handler(
        MessageHandler(
            filters.Document.ALL,
            file_handler
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            text_message
        )
    )

    return app