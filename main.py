from core.logger import logger

import tools.load_tools
from tools.registry import get_tools

from core.app import create_app


def show_tools():

    print("\n========== TOOLS ==========")

    for name in sorted(get_tools()):
        print(f"• {name}")

    print("===========================\n")


def main():

    logger.info("Loading tools...")

    show_tools()

    logger.info("Creating application...")

    app = create_app()

    print("""
========================================
            🤖 Jarvis AI
========================================
""")

    logger.info("Jarvis started.")

    app.run_polling()


if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        logger.info("Jarvis stopped.")

    except Exception as e:

        logger.exception(e)
