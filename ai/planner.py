import json
import ollama

from ai.prompt import SYSTEM_PROMPT
from ai.context import build_context

MODEL = "qwen2.5-coder:14b"


def clean_response(text):

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    # Някои модели добавят "assistant"
    for prefix in (
        "assistant",
        "Assistant",
        "ASSISTANT"
    ):

        if text.startswith(prefix):
            text = text[len(prefix):].strip()

    # Вземаме само JSON-а
    start = text.find("{")
    end = text.rfind("}")

    if start != -1 and end != -1:
        text = text[start:end + 1]

    return text


def create_plan(message):

    prompt = f"""
{SYSTEM_PROMPT}

{build_context()}

===== USER =====

{message}

Върни само JSON.
"""

    response = ollama.chat(

        model=MODEL,

        options={
            "temperature": 0
        },

        messages=[

            {
                "role": "system",
                "content": prompt
            },

            {
                "role": "user",
                "content": message
            }

        ]

    )

    text = clean_response(
        response["message"]["content"]
    )

    # Debug
    print("\n========== RAW MODEL ==========")
    print(text)
    print("================================\n")

    # Ако няма JSON
    if "{" not in text or "}" not in text:

        return {
            "thought": "",
            "actions": [],
            "answer": text
        }

    try:

        return json.loads(text)

    except Exception as e:

        print("\n========== INVALID JSON ==========")
        print(e)
        print(text)
        print("==================================\n")

        return {
            "thought": "",
            "actions": [],
            "answer": text
        }