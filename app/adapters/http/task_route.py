from fastapi import APIRouter, Depends
from app.adapters.database.memory.repositories import TaskRepository
from app.domain.entities import TaskCreate, TaskRead
from app.use_case.task import TaskUseCase

router = APIRouter()

task_repository = TaskRepository()
def get_task_repository():
    return task_repository

@router.post("/tasks/", response_model=TaskRead)
async def create_task(
    task: TaskCreate, 
    task_repository: TaskRepository = Depends(get_task_repository)
):
    task_use_case = TaskUseCase(task_repository)
    return await task_use_case.create_task(task)

@router.get("/tasks/", response_model=list[TaskRead])
def list_tasks(
    task_repository: TaskRepository = Depends(get_task_repository)
):
    task_use_case = TaskUseCase(task_repository)
    return task_use_case.list_tasks()