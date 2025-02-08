from boto3.dynamodb.conditions import Key
import boto3
from botocore.exceptions import ClientError
from src.models.task import Task

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def add_task(task: Task):
    try:
        response = table.put_item(
            Item={
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'status': task.status
            }
        )
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None

def get_all_tasks():
    try:
        response = table.scan()
        return response['Items']
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None

def update_task(task_id: str, updated_task: Task):
    try:
        response = table.update_item(
            Key={'id': task_id},
            UpdateExpression="set title=:t, description=:d, status=:s",
            ExpressionAttributeValues={
                ':t': updated_task.title,
                ':d': updated_task.description,
                ':s': updated_task.status
            },
            ReturnValues="UPDATED_NEW"
        )
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None

def delete_task(task_id: str):
    try:
        response = table.delete_item(
            Key={'id': task_id}
        )
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None