from pydantic import BaseModel

class ProductsDTO(BaseModel):
    id : int
    name : str
    price : float = 0.00 
    description : str