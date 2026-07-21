import webbrowser


def open(url):

    webbrowser.open(url)

    return "Браузърът е отворен."


def search(query):

    url = (
        "https://www.google.com/search?q="
        + query
    )

    webbrowser.open(url)

    return "Търсенето е направено."