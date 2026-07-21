def read_file(path):

    try:

        with open(path, "r", encoding="utf-8") as f:

            return {
                "status": "success",
                "path": path,
                "content": f.read()
            }

    except UnicodeDecodeError:

        return {
            "status": "binary",
            "path": path
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }