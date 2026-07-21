def write_file(path, content):

    try:

        with open(path, "w", encoding="utf-8") as f:

            f.write(content)

        return {
            "status": "success",
            "path": path
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }