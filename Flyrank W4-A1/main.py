
from fastapi import FastAPI
from SRC.tasks.routers import task_router
from SRC.utils.db import Base, engine, localsession
from SRC.tasks.models import TaskModel
from SRC.auth.protected_routers import public_router, protected_router
from SRC.auth.routers import auth_router

Base.metadata.create_all(engine)

# Seed 3 example tasks only if the table is empty
db = localsession()
try:
    if db.query(TaskModel).count() == 0:
        db.add_all([
            TaskModel(name="Buy groceries", info="Milk, eggs, bread", is_complete=False),
            TaskModel(name="Write report", info="Q3 summary for team", is_complete=False),
            TaskModel(name="Call dentist", info="Reschedule appointment", is_complete=True),
        ])
        db.commit()
finally:
    db.close()

app = FastAPI(title="User data manager", description="Assignment NO 2 at FlyRank")
app.include_router(task_router)
app.include_router(auth_router)

app.include_router(public_router)
app.include_router(protected_router)