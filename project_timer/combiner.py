from project_timer.task import Task
from project_timer.timer import Timer
from project_timer.user import User


class Combiner:
    def __init__(self, name: str, id: int):
        self.user = User(name, id)

    def usr(self):
        return self.user

    # def start_task(self, task_name: str):
    #     task = Task(task_name, self.user)
    #
    #     timer = Timer(self.user)
    #     timer.start()
    #     task.id()
    #
    # def stop_task(self, task_name: str):
    #     pass