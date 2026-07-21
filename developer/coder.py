import ollama

SYSTEM = """
Ти си Senior Python Developer.

Поправяш грешки.

Никога не обяснявай.

Връщай само новия код.

Не използвай markdown.
"""


def improve(code, error):

    response = ollama.chat(

        model="llama3.1",

        messages=[

            {
                "role": "system",
                "content": SYSTEM
            },

            {
                "role": "user",
                "content": f"""
Грешка:

{error}

Код:

{code}
"""
            }

        ]

    )

    return response["message"]["content"]