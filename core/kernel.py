from core.logger import logger
from core.events import bus
from core.tasks import queue
from core.state import state


class Kernel:

    def __init__(self):

        logger.info("Kernel initialized")

    def start(self):

        logger.info("Kernel started")

        state.set("running", True)

        bus.emit("kernel.started")

    def stop(self):

        logger.info("Kernel stopped")

        state.set("running", False)

        bus.emit("kernel.stopped")

    def add_task(self, task):

        queue.add(task)

        bus.emit("task.created", task)

    def next_task(self):

        return queue.next()


kernel = Kernel()