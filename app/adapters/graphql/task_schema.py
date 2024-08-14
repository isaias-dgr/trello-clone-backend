import graphene
from graphene_pydantic import PydanticObjectType, PydanticInputObjectType
from app.adapters.database.dynamodb.repositories import TaskRepository
from app.domain.entities import TaskRead, TaskCreate, TaskMove
from app.use_case.task import TaskUseCase


task_repository = TaskRepository("Trello_Clone")

class TaskType(PydanticObjectType):
    class Meta:
        model = TaskRead

class TaskCreateInput(PydanticInputObjectType):
    class Meta:
        model = TaskCreate


class TaskMoveInput(PydanticInputObjectType):
    class Meta:
        model = TaskMove

class Query(graphene.ObjectType):
    all_tasks = graphene.List(TaskType)

    def resolve_all_tasks(self, info):
        task_use_case = TaskUseCase(task_repository)
        return task_use_case.list_tasks()

class CreateTask(graphene.Mutation):
    class Arguments:
        input = TaskCreateInput(required=True)

    task = graphene.Field(TaskType)

    async def mutate(self, info, input):
        input.pop("id",None)
        input.pop("created_at",None)
        input.pop("updated_at",None)
        new_task = TaskCreate(**input)
        task_use_case = TaskUseCase(task_repository)
        task = await task_use_case.create_task(new_task)
        return CreateTask(task=task)
    
class MoveTask(graphene.Mutation):
    class Arguments:
        input = TaskMoveInput(required=True)

    task = graphene.Field(TaskType)

    async def mutate(self, info, input):
        new_task = TaskMove(**input)
        task_use_case = TaskUseCase(task_repository)
        task = await task_use_case.move_task(new_task)
        return CreateTask(task=task)

class Mutation(graphene.ObjectType):
    create_task = CreateTask.Field()
    move_task = MoveTask.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)