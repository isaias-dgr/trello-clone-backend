import boto3
from botocore.exceptions import ClientError

# Crear cliente de DynamoDB
dynamodb = boto3.resource('dynamodb')

# Nombre de la tabla DynamoDB
table_name = 'Trello_Clone'

# Referencia a la tabla
table = dynamodb.Table(table_name)

# Lista de tareas a insertar
tasks = [
    {
        "id": "e24e2289-6d68-4285-a022-71eddf7ecce4",
        "position": 0,
        "status": "todo",
        "statusLabel": "To Do",
        "depto": "Backend",
        "title": "Develop API endpoints",
        "description": "Develop API endpoints for Backend department.",
        "comments": [],
        "attachments": [],
        "createdAt": "2024-08-13T19:28:47.728320",
        "updatedAt": "2024-08-13T19:28:47.728332",
        
    },
    {
        "id": "c18c7f25-86d9-478e-b10e-2a9bc908a52d",
        "position": 0,
        "status": "inProgress",
        "statusLabel": "In Progress",
        "depto": "Frontend",
        "title": "Design new user interface",
        "description": "Design new user interface for Frontend department.",
        "comments": [],
        "attachments": [],
        "createdAt": "2024-08-13T19:29:01.738232",
        "updatedAt": "2024-08-13T19:29:01.738244",
        
    },
    {
        "id": "8b678f5a-17f2-4267-93c3-508e769b21ef",
        "position": 0,
        "status": "done",
        "statusLabel": "Done",
        "depto": "Full Stack",
        "title": "Integrate frontend with backend",
        "description": "Integrate frontend with backend for Full Stack department.",
        "comments": [],
        "attachments": [],
        "createdAt": "2024-08-13T19:29:13.748211",
        "updatedAt": "2024-08-13T19:29:13.748223",
        
    },
]

# Insertar las tareas en la tabla DynamoDB
for task in tasks:
    try:
        table.put_item(Item=task)
        print(f"Tarea con ID {task['id']} guardada exitosamente.")
    except ClientError as e:
        print(f"Error al guardar la tarea con ID {task['id']}: {e.response['Error']['Message']}")