def replace_text(file, old, new):

    with open(file, "r", encoding="utf-8") as f:

        text = f.read()

    text = text.replace(old, new)

    with open(file, "w", encoding="utf-8") as f:

        f.write(text)

    return True