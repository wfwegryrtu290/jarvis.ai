import os


def get_type(path):

    ext = os.path.splitext(path)[1].lower()

    if ext in (
        ".py",".js",".cpp",".c",".cs",".java",
        ".php",".html",".css",".json",".xml",
        ".txt",".md",".ini",".yaml",".yml"
    ):
        return "text"

    elif ext in (
        ".png",".jpg",".jpeg",".bmp",
        ".gif",".webp",".svg"
    ):
        return "image"

    elif ext in (
        ".mp4",".avi",".mov",".mkv",".wmv"
    ):
        return "video"

    elif ext in (
        ".mp3",".wav",".ogg",".flac",".m4a"
    ):
        return "audio"

    elif ext in (
        ".pdf",".docx",".xlsx",".pptx"
    ):
        return "office"

    elif ext in (
        ".zip",".rar",".7z"
    ):
        return "archive"

    return "unknown"