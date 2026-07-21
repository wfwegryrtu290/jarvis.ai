import json

from core.logger import logger
from core.kernel import kernel

from ai.planner import create_plan
from ai.validator import validate

from agents.manager import manager


def process(message):

    logger.info(f"📩 {message}")

    kernel.add_task(message)

    try:

        # ==========================
        # Planning
        # ==========================

        logger.info("📋 Creating plan...")

        plan = create_plan(message)

        logger.debug(plan)

        # ==========================
        # Validate
        # ==========================

        ok, error = validate(plan)

        if not ok:

            logger.error(error)

            return error

        # ==========================
        # Execute
        # ==========================

        logger.info("⚙ Executing actions...")

        results = []

        for action in plan.get("actions", []):

            result = manager.execute(action)

            results.append(result)

        # ==========================
        # Check results
        # ==========================

        for result in results:

            if not isinstance(result, dict):
                continue

            if result.get("success") is False:

                logger.error(result)

                return result.get(
                    "error",
                    "Възникна грешка."
                )

            if "report" in result:

                report = result["report"]

                if isinstance(report, dict):

                    return json.dumps(
                        report,
                        ensure_ascii=False,
                        indent=4
                    )

                return str(report)

            if "message" in result:

                return str(result["message"])

        # ==========================
        # Final Answer
        # ==========================

        answer = str(plan.get("answer", "")).strip()

        if not answer:

            answer = "Готово."

        return answer

    except Exception as e:

        logger.exception(e)

        return "Възникна вътрешна грешка."