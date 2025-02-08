from fastapi import APIRouter
from src.services.dynamodb_service import get_all_tasks
from src.utils.response import success_response, error_response

router = APIRouter()

@router.get("/tasks")
async def list_tasks():
    try:
        tasks = await get_all_tasks()
        return success_response(data=tasks)
    except Exception as e:
        return error_response(message=str(e))