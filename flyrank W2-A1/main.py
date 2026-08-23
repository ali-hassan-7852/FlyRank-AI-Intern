
from fastapi import FastAPI
from SRC.tasks.routers import task_router
from SRC.utils.db import Base, engine

Base.metadata.create_all(engine)

app = FastAPI(title="User data manager",description="Assignment NO 2 at FlyRank")
app.include_router(task_router)

