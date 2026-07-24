from core.logger import logger


class AgentLoop:

    def __init__(self):

        self.running = False
        self.max_steps = 10

    def run(self, planner, executor, observer=None):

        self.running = True

        step = 0

        while self.running:

            if step >= self.max_steps:

                logger.warning("Maximum agent steps reached.")

                break

            plan = planner()

            if not plan:

                logger.info("Planner returned no actions.")

                break

            logger.info(f"Step {step + 1}")

            result = executor(plan)

            if observer:

                if observer(plan, result):

                    logger.info("Goal completed.")

                    break

            step += 1

        self.running = False

    def stop(self):

        self.running = False


agent_loop = AgentLoop()
