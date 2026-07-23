import json
import time

from core.logger import logger
from core.kernel import kernel

from ai.planner import create_plan
from ai.validator import validate

from agents.manager import manager


def process(message):

    start = time.perf_counter()

    logger.info(f"📩 {message}")

    try:

        kernel.add_task(message)

        logger.info("📋 Creating plan...")

        plan = create_plan(message)

        logger.debug(plan)

        if not isinstance(plan, dict):

            return "Planner върна невалиден резултат."

        ok, error = validate(plan)

        if not ok:

            logger.error(error)

            return error

        logger.info("⚙ Executing actions...")

        actions = plan.get("actions", [])

        if not isinstance(actions, list):

            return "Невалиден списък с действия."

        results = []

        for action in actions:

            result = manager.execute(action)

            results.append(result)

        kernel.last_results = results

        messages = []

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

                messages.append(str(result["message"]))

        if messages:

            return "\n".join(messages)

        answer = str(plan.get("answer", "")).strip()

        if not answer:

            answer = "Готово."

        elapsed = round(
            time.perf_counter() - start,
            3
        )

        logger.info(f"✅ Finished in {elapsed}s")

        return answer

    except Exception as e:

        logger.exception(e)

        return "Възникна вътрешна грешка."
