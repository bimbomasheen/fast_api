from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel


app = FastAPI()


# MODELS #
class Item(BaseModel):
    name: str
    price: float
    brand: str|None = None

class UpdateItem(BaseModel):
    name: str|None = None
    price: float|None = None
    brand: str|None = None

inventory = {}


# ROUTES #
@app.get("/")
def home():
    return {"Hello": "World"}

@app.get("/items/")
def get_items():
    return inventory

@app.get("/items/{item_id}")
def get_item_by_id(item_id: int = Path(title="Item ID", description="The ID of the item.")):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found.")
    return inventory[item_id]

@app.get("/items/by-name/")
def get_item_by_name(name: str = Query(title="Name", description="The name of the item.")):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=404, detail="Item not found.")

@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="Item already exists.")
    inventory[item_id] = item
    return inventory[item_id]

@app.put("/items/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found.")
    if item.name:
        inventory[item_id].name = item.name
    if item.price:
        inventory[item_id].price = item.price
    if item.brand:
        inventory[item_id].brand = item.brand
    return inventory[item_id]

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found.")
    del inventory[item_id]
    return {"Message": "Item deleted."}