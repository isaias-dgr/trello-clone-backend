import boto3
from typing import List
from app.domain.entities import TaskCreate, TaskRead, TaskMove
from app.ports.repository import ITaskRepository
from boto3.dynamodb.conditions import Key

class TaskRepository(ITaskRepository):
    def __init__(self, table_name: str):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(table_name)
        self.client = boto3.client('dynamodb')

    def create_task(self, task: TaskCreate) -> TaskRead:
        task_item = task.dict()
        task_item["id"] = str(task_item["id"])
        task_item["created_at"] = task_item["created_at"].isoformat()
        task_item["updated_at"] = task_item["updated_at"].isoformat()
        self.table.put_item(Item=task_item)
        
        return TaskRead(**task_item)

    def get_tasks(self) -> List[TaskRead]:
        response = self.table.scan()
        items = response.get('Items', [])
        tasks = [TaskRead(**item) for item in items]
        return tasks
    
    def get_by_ids(self, ids: List[str]) -> List[TaskRead]:
        tasks = []
        response = self.client.batch_get_item(
            RequestItems={
                self.table.name: {
                    'Keys': [{'id': {'S': str(id)}} for id in ids],
                }
            }
        )
        items = response.get('Responses', {}).get(self.table.name, [])
        tasks = [TaskRead(**self._simplify_dynamodb_item(item)) for item in items]
        return tasks
    
    def move_task(self, task: TaskMove) -> TaskRead:
        respose = self.table.update_item(
            Key={"id": str(task.id)},
            UpdateExpression="set #statusField = :newStatus, #positionField = :newPosition",
            ExpressionAttributeNames={
                "#statusField": "status",
                "#positionField": "position"
            },
            ExpressionAttributeValues={
                ':newStatus': task.status,
                ':newPosition': task.position
            },
            ReturnValues="ALL_NEW" 
        )
        return TaskRead(**respose['Attributes'])

    def _simplify_dynamodb_item(self, item):
        """Convierte un ítem de DynamoDB a un diccionario sin tipos de datos."""
        return {k: list(v.values())[0] for k, v in item.items()}
