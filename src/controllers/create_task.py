def create_task(task_data):
    import boto3
    from botocore.exceptions import ClientError
    from src.services.dynamodb_service import add_task

    try:
        task = add_task(task_data)
        return {
            "statusCode": 201,
            "body": {
                "message": "Task created successfully",
                "task": task
            }
        }
    except ClientError as e:
        return {
            "statusCode": 500,
            "body": {
                "message": "Error creating task",
                "error": str(e)
            }
        }