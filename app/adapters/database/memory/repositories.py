# app/adapters/memory/task_repository_in_memory.py
from typing import List
from uuid import uuid4
from app.domain.entities import TaskCreate, TaskRead
from app.ports.repository import ITaskRepository

class TaskRepository(ITaskRepository):

    def __init__(self):
        self.tasks = []
        self.current_id = uuid4()

    def create_task(self, task: TaskCreate) -> TaskRead:
        task_read = TaskRead( **task.dict())
        self.tasks.append(task_read)
        return task_read

    def get_tasks(self) -> List[TaskRead]:
        return self.tasks