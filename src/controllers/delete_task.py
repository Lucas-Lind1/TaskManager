def delete_task(task_id: str):
    import boto3
    from botocore.exceptions import ClientError
    from src.services.dynamodb_service import delete_task_from_dynamodb
    from src.utils.response import success_response, error_response

    try:
        delete_task_from_dynamodb(task_id)
        return success_response({"message": "Task deleted successfully."})
    except ClientError as e:
        return error_response(f"Failed to delete task: {str(e)}")