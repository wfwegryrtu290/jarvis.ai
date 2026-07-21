from memory.memory import create_memory
from developer.memory import create as create_developer_memory

from developer.agent import developer

from core.kernel import kernel

from windows.application_scanner import scanner

from computer.scanner import scan


def startup():

    print("🧠 Initializing memory...")

    create_memory()
    create_developer_memory()

    print("⚙ Starting kernel...")

    kernel.start()

    # ==========================
    # Scan installed applications
    # ==========================

    print("🖥 Scanning installed applications...")

    apps = scanner.scan()

    print(f"🟢 Applications: {len(apps)}")

    # ==========================
    # Scan computer
    # ==========================

    print("💻 Scanning computer...")

    computer = scan()

    print(f"🟢 Applications : {len(computer.apps)}")
    print(f"📄 Files        : {len(computer.files)}")
    print(f"📁 Folders      : {len(computer.folders)}")

    # ==========================
    # Scan workspace
    # ==========================

    print("📂 Scanning workspace...")

    developer.scan(".")

    stats = developer.stats()

    print()

    print(f"📂 Python Files : {stats['python_files']}")
    print(f"📑 Indexed Files: {stats['indexed_files']}")
    print(f"🧩 Dependencies : {stats['dependency_files']}")
    print(f"🔍 Symbols      : {stats['symbol_files']}")

    print()

    print("✅ Startup completed.")