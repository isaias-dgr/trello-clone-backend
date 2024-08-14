# app/use_case/task_use_case.py
from app.domain.entities import TaskCreate, TaskRead, TaskMove
from app.ports.repository import ITaskRepository
from functools import reduce


class TaskUseCase:
    def __init__(self, repository: ITaskRepository):
        self.repository = repository

    async def create_task(self, task_data: TaskCreate) -> TaskRead:
        task = self.repository.create_task(task_data)
        return task

    async def move_task(self, task_data: TaskMove) -> TaskRead:
        next_to_move = None
        position = 0 

        if task_data.prev_to and task_data.next_to:
            next_to_move = self.repository.get_by_ids([task_data.next_to,task_data.prev_to])
            position = reduce (lambda acc, item: acc + item.position, next_to_move, 0) / 2

        if task_data.prev_to and task_data.next_to is None:
            next_to_move = self.repository.get_by_ids([task_data.prev_to])
            position = int( next_to_move[0].position) + 1

        if task_data.prev_to is None and task_data.next_to:
            next_to_move = self.repository.get_by_ids([task_data.next_to])
            position = int(next_to_move[0].position) - 1

        task_data.position = position
        task = self.repository.move_task(task_data)
        return task


    def list_tasks(self):
        return self.repository.get_tasks()