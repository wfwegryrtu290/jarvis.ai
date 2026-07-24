from core.logger import logger


class LoopObserver:

    def check(self, action, result):

        if result is None:

            logger.warning("Observer: empty result")

            return False

        if not isinstance(result, dict):

            logger.warning("Observer: invalid result")

            return False

        if result.get("success") is False:

            logger.warning(
                f"Action failed: {result.get('error')}"
            )

            return False

        logger.info("Action completed successfully.")

        return True

    def goal_completed(self, plan):

        actions = plan.get("actions", [])

        return len(actions) == 0


observer = LoopObserver()
