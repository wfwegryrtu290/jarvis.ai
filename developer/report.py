from developer.analyzer import analyze


def create_report(report):

    text = []

    text.append("📋 Developer Report")
    text.append("")

    text.append(f"Проверени файлове: {report['files']}")
    text.append("")

    if report["success"]:

        text.append("✅ Не са открити синтактични грешки.")

    else:

        text.append("❌ Намерени са грешки.")
        text.append("")
        text.append(analyze(report))

    return "\n".join(text)