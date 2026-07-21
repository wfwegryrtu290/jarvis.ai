import psutil

def get_pc_info():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    return (
        f"💻 CPU: {cpu}%\n"
        f"🧠 RAM: {ram.used / (1024**3):.1f} GB / {ram.total / (1024**3):.1f} GB\n"
        f"💾 Disk: {disk.percent}%"
    )