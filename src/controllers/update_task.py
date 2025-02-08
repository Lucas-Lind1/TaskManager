from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.dynamodb_service import update_task as update_task_service

router = APIRouter()

class TaskUpdate(BaseModel):
    title: str
    description: str
    status: str

@router.put("/tasks/{task_id}")
async def update_task(task_id: str, task_update: TaskUpdate):
    try:
        updated_task = update_task_service(task_id, task_update.dict())
        if not updated_task:
            raise HTTPException(status_code=404, detail="Task not found")
        return updated_task
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))