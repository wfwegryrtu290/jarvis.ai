import re


OPEN = [
    "отвори",
    "стартирай",
    "пусни"
]

READ = [
    "прочети",
    "какво има във",
    "какво има в",
    "какво пише",
    "съдържанието"
]

LIST = [
    "какво има тук",
    "какво има вътре",
    "покажи съдържанието",
    "изброй"
]

ACTIVATE = [
    "покажи",
    "покажи отпред",
    "активирай",
    "фокусирай"
]

CLOSE = [
    "затвори",
    "спри"
]


def _extract_target(message, keyword):

    text = message.lower()

    index = text.find(keyword)

    if index == -1:
        return None

    target = text[index + len(keyword):].strip()

    if not target:
        return None

    return target


def resolve(message):

    text = message.lower().strip()

    # OPEN

    for word in OPEN:

        if text.startswith(word):

            target = _extract_target(text, word)

            if target:

                return {

                    "handled": True,

                    "plan": {

                        "thought": "Локално разпозната команда.",

                        "actions": [

                            {

                                "agent": "system",

                                "tool": "computer.open",

                                "arguments": {

                                    "target": target

                                }

                            }

                        ],

                        "answer": ""

                    }

                }

    # READ

    if text.startswith("прочети"):

        target = text.replace("прочети", "").strip()

        return {

            "handled": True,

            "plan": {

                "thought": "Локално разпозната команда.",

                "actions": [

                    {

                        "agent": "system",

                        "tool": "computer.read",

                        "arguments": {

                            "target": target

                        }

                    }

                ],

                "answer": ""

            }

        }

    # LIST

    if "какво има вътре" in text or "покажи съдържанието" in text:

        return {

            "handled": True,

            "plan": {

                "thought": "Локално разпозната команда.",

                "actions": [

                    {

                        "agent": "system",

                        "tool": "computer.list",

                        "arguments": {}

                    }

                ],

                "answer": ""

            }

        }

    # ACTIVATE

    if "отпред" in text:

        target = text.replace("покажи", "").replace("отпред", "").strip()

        return {

            "handled": True,

            "plan": {

                "thought": "Локално разпозната команда.",

                "actions": [

                    {

                        "agent": "system",

                        "tool": "computer.activate",

                        "arguments": {

                            "target": target

                        }

                    }

                ],

                "answer": ""

            }

        }

    # CLOSE

    if text.startswith("затвори"):

        target = text.replace("затвори", "").strip()

        return {

            "handled": True,

            "plan": {

                "thought": "Локално разпозната команда.",

                "actions": [

                    {

                        "agent": "system",

                        "tool": "computer.close",

                        "arguments": {

                            "target": target

                        }

                    }

                ],

                "answer": ""

            }

        }

    return {

        "handled": False

    }
