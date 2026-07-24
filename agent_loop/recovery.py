from core.logger import logger


class Recovery:

    def __init__(self):

        self.errors = []

    def reset(self):

        self.errors.clear()

    def register(self, action, result):

        error = {
            "action": action,
            "result": result,
        }

        self.errors.append(error)

        logger.warning(
            f"Recovery registered error: {result.get('error', 'Unknown error')}"
        )

    def should_retry(self, action, result):

        if result is None:
            return False

        if result.get("success", False):
            return False

        count = 0

        for error in self.errors:

            if error["action"] == action:
                count += 1

        # Максимум 3 опита
        return count < 3

    def recover(self, action, result):

        self.register(action, result)

        if self.should_retry(action, result):

            logger.info("Retrying action...")

            return {
                "retry": True,
                "action": action,
            }

        logger.error("Recovery failed.")

        return {
            "retry": False,
            "error": result.get(
                "error",
                "Unknown error."
            ),
        }

    def history(self):

        return list(self.errors)


recovery = Recovery()
