from SRC.tasks.dtos import taskSchema
from sqlalchemy.orm import session
from SRC.tasks.models import TaskModel
from fastapi import HTTPException



def create_task(body: taskSchema, db: session):
    data = body.model_dump()
    new_task = TaskModel(name= data["name"],
                        info = data["info"],
                        is_complete = data["is_complete"])
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return {
        " status": "Task created successfully",
        "data": new_task
    }
    
def get_task(db: session):
    tasks = db.query(TaskModel).all()
    
    return {
        "status": "Tasks retrieved successfully",
        "data": tasks
    }
    
    
def get_one_task(task_id: int, db: session):
    one_task = db.query(TaskModel).get(task_id)
    
    if not one_task:
        return HTTPException(404, detail="Task not found")
    
    return {
        "status": "Task retrieved successfully",
        "data": one_task}
    
def update_task(body: taskSchema, task_id: int, db: session):
    one_task = db.query(TaskModel).get(task_id)
        
    if not one_task:
        return HTTPException(404, detail="Task not found")
    
    one_task.name = body.name
    one_task.info = body.info
    one_task.is_complete = body.is_complete
    
    db.add(one_task)
    db.commit()
    db.refresh(one_task)
        
    return {
            "status": "Tasks Updated successfully",
            "data": one_task
        }
    
def delete_task(task_id: int, db: session):
    
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        return HTTPException(404, detail="Task not found")
    
    db.delete(one_task)
    db.commit()

    return {
        "status": "Task deleted successfully"
    }