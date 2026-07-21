from agents.manager import manager

from core.queue import task_queue


def process_queue():

    while not task_queue.empty():

        task = task_queue.get()

        task.status = "running"

        manager.execute({

            "agent": task.agent,

            "tool": task.tool,

            "arguments": task.arguments

        })

        task.status = "finished"