from fastapi import FastAPI
from controllers.create_task import create_task
from controllers.list_tasks import list_tasks
from controllers.update_task import update_task
from controllers.delete_task import delete_task

app = FastAPI()

@app.post("/tasks", response_model=dict)
def add_task(task: dict):
    return create_task(task)

@app.get("/tasks", response_model=list)
def get_tasks():
    return list_tasks()

@app.put("/tasks/{task_id}", response_model=dict)
def modify_task(task_id: str, task: dict):
    return update_task(task_id, task)

@app.delete("/tasks/{task_id}", response_model=dict)
def remove_task(task_id: str):
    return delete_task(task_id)