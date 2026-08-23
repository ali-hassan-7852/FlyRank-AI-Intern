from sqlalchemy import Column, Integer, Boolean, String
from SRC.utils.db import Base

class TaskModel(Base):
    __tablename__ = "User_Data"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    info = Column(String)
    is_complete = Column(Boolean, default=False)