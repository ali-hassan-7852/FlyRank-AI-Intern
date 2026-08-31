from pydantic import BaseModel

class  taskSchema(BaseModel):
    
    name: str
    info: str
    is_complete: bool=False