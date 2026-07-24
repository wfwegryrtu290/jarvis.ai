from core.logger import logger
from core.events import bus
from core.tasks import queue
from core.state import state


class Kernel:

    def __init__(self):

        self.task_count = 0
        self.completed_tasks = 0
        self.failed_tasks = 0

        self.current_task = None

        self.last_results = []

        logger.info("Kernel initialized")

    # ==========================
    # Lifecycle
    # ==========================

    def start(self):

        logger.info("Kernel started")

        state.set("running", True)

        bus.emit("kernel.started")

    def stop(self):

        logger.info("Kernel stopped")

        state.set("running", False)

        bus.emit("kernel.stopped")

    def is_running(self):

        return state.get("running", False)

    # ==========================
    # Tasks
    # ==========================

    def add_task(self, task):

        self.task_count += 1

        self.current_task = task

        queue.add(task)

        bus.emit("task.created", task)

    def next_task(self):

        self.current_task = queue.next()

        return self.current_task

    def task_completed(self, result=None):

        self.completed_tasks += 1

        self.last_results.append(result)

        self.current_task = None

        bus.emit("task.completed", result)

    def task_failed(self, error):

        self.failed_tasks += 1

        self.current_task = None

        bus.emit("task.failed", error)

    # ==========================
    # Results
    # ==========================

    def clear_results(self):

        self.last_results.clear()

    def reset(self):

        self.task_count = 0
        self.completed_tasks = 0
        self.failed_tasks = 0

        self.current_task = None

        self.last_results.clear()

        logger.info("Kernel reset")

    # ==========================
    # Stats
    # ==========================

    def stats(self):

        return {

            "running": self.is_running(),

            "task_count": self.task_count,

            "completed_tasks": self.completed_tasks,

            "failed_tasks": self.failed_tasks,

            "queue_size": len(queue),

            "current_task": self.current_task,

            "last_results": len(self.last_results),

        }


kernel = Kernel()
