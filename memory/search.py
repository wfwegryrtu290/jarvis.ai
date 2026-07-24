from memory.memory import memory
from memory.history import history
from memory.knowledge import knowledge


def search_memory(query):

    if not query:
        return []

    query = query.lower().strip()

    results = []

    # ==========================
    # Conversation Memory
    # ==========================

    for item in memory.search(query):

        results.append({
            "source": "conversation",
            "data": item
        })

    # ==========================
    # Knowledge
    # ==========================

    for key, value in knowledge.all().items():

        text = f"{key} {value}".lower()

        if query in text:

            results.append({
                "source": "knowledge",
                "data": {
                    "key": key,
                    "value": value
                }
            })

    # ==========================
    # History
    # ==========================

    for item in history.all():

        text = str(item).lower()

        if query in text:

            results.append({
                "source": "history",
                "data": item
            })

    return results


def search_first(query):

    results = search_memory(query)

    if not results:
        return None

    return results[0]
