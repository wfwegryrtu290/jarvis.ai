import os

from workspace.indexer import index_workspace


TEXT_FILES = (
    ".txt",".md",".py",".json",".html",".css",".js",
    ".cpp",".c",".cs",".java",".php",".sql",".xml",
    ".yaml",".yml",".ini",".log",".csv"
)

OFFICE_FILES = (
    ".doc",".docx",".xls",".xlsx",".ppt",".pptx",".pdf",".odt"
)

IMAGES = (
    ".png",".jpg",".jpeg",".gif",".bmp",".webp",".svg",".ico",".tiff"
)

VIDEO = (
    ".mp4",".avi",".mkv",".mov",".wmv",".webm",".flv"
)

AUDIO = (
    ".mp3",".wav",".aac",".ogg",".m4a",".flac"
)

ARCHIVES = (
    ".zip",".rar",".7z",".tar",".gz"
)

EXECUTABLES = (
    ".exe",".msi",".bat",".cmd",".ps1"
)

ALL_SUPPORTED = (
    TEXT_FILES
    + OFFICE_FILES
    + IMAGES
    + VIDEO
    + AUDIO
    + ARCHIVES
    + EXECUTABLES
)


def file_type(ext):

    if ext in TEXT_FILES:
        return "text"

    if ext in OFFICE_FILES:
        return "office"

    if ext in IMAGES:
        return "image"

    if ext in VIDEO:
        return "video"

    if ext in AUDIO:
        return "audio"

    if ext in ARCHIVES:
        return "archive"

    if ext in EXECUTABLES:
        return "program"

    return "other"


def scan(path):

    data = []

    for root, dirs, files in os.walk(path):

        dirs[:] = [

            d for d in dirs

            if d not in (

                "__pycache__",
                ".git",
                ".venv",
                "venv",
                "node_modules"

            )
        ]

        for file in files:

            if file.lower().endswith(ALL_SUPPORTED):

                full = os.path.join(root,file)

                try:

                    stat = os.stat(full)

                    ext = os.path.splitext(file)[1].lower()

                    data.append({

                        "path": full,
                        "name": file,
                        "extension": ext,
                        "type": file_type(ext),
                        "size": stat.st_size,
                        "modified": stat.st_mtime

                    })

                except:
                    pass

    index_workspace(data)

    return data