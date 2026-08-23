
from fastapi import FastAPI,Request
from dtos import ProductsDTO
from mockdata import Products

app = FastAPI()

@app.get("/all_Products")
def all_products():
    return Products


@app.get("/Product/{product_id}")
def get_one_product(product_id: int):

    for oneProduct in Products:
        if oneProduct.get("id") == product_id:
            return oneProduct
    return {
            "Error": "This product does not found for this ID!"
    }
        
@app.get("/greet")
def greet_fun(request:Request):
    query_params = dict(request.query_params)
    print(query_params)
    
    return {
        "Greet": f"The name is {query_params.get("name")} , Your age is {query_params.get("age")}"
    }
    
@ app.post("/addProduct")
def add_product(product_data: ProductsDTO):
    product_data = product_data.model_dump()
    Products.append(product_data)
    return {"status": "Product added successfully",
            "data": Products}
    
@app.put("/updateProduct/{product_id}")
def update_data(product_data: ProductsDTO, product_id: int):

    for index, one_product in enumerate(Products):
        if one_product.get("id") == product_id:
            Products[index] = product_data.model_dump()
            return {
                "final msg" : "Product added successfully",
                "Product" : product_data
            } 
    return {
                    "Error": "This product does not found for this ID!"
            }

@app.delete("/deleteProduct/{product_id}")
def del_product(product_id: int):
    for index, one_product in enumerate(Products):
        if one_product.get("id") == product_id:
            deleted_product = Products.pop(index)
            
    return {
            "status": "Product deleted successfully",
                            "data": deleted_product
            }
            