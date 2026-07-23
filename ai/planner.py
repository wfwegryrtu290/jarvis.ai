import json
import ollama

from core.logger import logger

from ai.prompt import SYSTEM_PROMPT
from ai.context import build_context

MODEL = "qwen2.5-coder:14b"


def clean_response(text: str) -> str:

    if not text:
        return ""

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    for prefix in (
        "assistant",
        "Assistant",
        "ASSISTANT",
    ):

        if text.startswith(prefix):
            text = text[len(prefix):].strip()

    start = text.find("{")
    end = text.rfind("}")

    if start != -1 and end != -1:
        text = text[start:end + 1]

    return text.strip()


def fallback(answer: str):

    return {
        "thought": "",
        "actions": [],
        "answer": answer.strip()
    }


def create_plan(message):

    prompt = f"""
{SYSTEM_PROMPT}

{build_context()}

===== USER =====

{message}

Върни само JSON.
"""

    try:

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

    except Exception as e:

        logger.exception(e)

        return fallback(
            "Не успях да се свържа с AI модела."
        )

    content = (
        response
        .get("message", {})
        .get("content", "")
    )

    text = clean_response(content)

    logger.debug(text)

    if not text:
        return fallback("")

    if "{" not in text or "}" not in text:
        return fallback(text)

    try:

        plan = json.loads(text)

        if not isinstance(plan, dict):
            return fallback(text)

        plan.setdefault("thought", "")
        plan.setdefault("actions", [])
        plan.setdefault("answer", "")

        return plan

    except Exception as e:

        logger.exception(e)

        return fallback(text)
