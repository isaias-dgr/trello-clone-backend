import boto3

dynamodb = boto3.client('dynamodb')
table_name = 'Trello_Clone'

response = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'  # Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'  # UUID (String)
        },
        {
            'AttributeName': 'position',
            'AttributeType': 'N'  # Float (Number)
        },
        {
            'AttributeName': 'status',
            'AttributeType': 'S'  # String
        },
        {
            'AttributeName': 'depto',
            'AttributeType': 'S'  # String
        },
        {
            'AttributeName': 'user_id',
            'AttributeType': 'S'  # UUID (String)
        }
    ],
    GlobalSecondaryIndexes=[
        {
            'IndexName': 'positionIndex',
            'KeySchema': [
                {
                    'AttributeName': 'position',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            'Projection': {
                'ProjectionType': 'ALL'
            },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        },
        {
            'IndexName': 'statusIndex',
            'KeySchema': [
                {
                    'AttributeName': 'status',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            'Projection': {
                'ProjectionType': 'ALL'
            },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        },
        {
            'IndexName': 'deptoIndex',
            'KeySchema': [
                {
                    'AttributeName': 'depto',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            'Projection': {
                'ProjectionType': 'ALL'
            },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        },
        {
            'IndexName': 'userIndex',
            'KeySchema': [
                {
                    'AttributeName': 'user_id',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            'Projection': {
                'ProjectionType': 'ALL'
            },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print(f"Table {table_name} created successfully.")