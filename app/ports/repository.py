# app/domain/interfaces.py
from abc import ABC, abstractmethod
from typing import List
from app.domain.entities import TaskCreate, TaskRead, TaskMove

class ITaskRepository(ABC):
    @abstractmethod
    def create_task(self, task: TaskCreate) -> TaskRead:
        pass

    @abstractmethod
    def get_tasks(self) -> List[TaskRead]:
        pass

    @abstractmethod
    def move_task(self, task: TaskMove) -> TaskRead:
        pass

    @abstractmethod
    def get_by_ids(self, ids: List[str]) -> List[TaskRead]:
        pass