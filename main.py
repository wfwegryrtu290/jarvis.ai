import tools
import tools.load_tools
from tools.registry import get_tools

print("\n===== TOOLS =====")

for name in get_tools():
    print(name)

print("=================\n")

from core.app import create_app

app = create_app()

print("""
=====================================
        🤖 Jarvis AI
=====================================
""")

app.run_polling()
