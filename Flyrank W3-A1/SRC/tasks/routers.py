from SRC.utils.db import get_db
from SRC.tasks import controllers
from SRC.tasks.dtos import taskSchema
from fastapi import APIRouter, Depends

from SRC.tasks.dtos import taskSchema

task_router = APIRouter(prefix="/tasks")

@task_router.post("/create")
def create_task(body: taskSchema, db=Depends(get_db)):
    return controllers.create_task(body, db)

@task_router.get("/get_tasks")
def get_task(db=Depends(get_db)):
    return controllers.get_task(db)

@task_router.get("/one_task/{task_id}")
def get_one_task(task_id: int, db=Depends(get_db)):
    return controllers.get_one_task(task_id,db)

@task_router.put("/update_task/{task_id}")
def update_task(body: taskSchema, task_id: int, db=Depends(get_db)):
    return controllers.update_task(body, task_id, db)

@task_router.delete("/delete_task/{task_id}")
def delete_task(task_id: int, db=Depends(get_db)):
    return controllers.delete_task(task_id, db)