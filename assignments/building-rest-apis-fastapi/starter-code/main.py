from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Dict

app = FastAPI(title="Items API - Starter")


class Item(BaseModel):
    name: str = Field(..., example="Notebook")
    description: Optional[str] = Field(None, example="200 pages")
    price: float = Field(..., ge=0, example=3.5)


# In-memory store: item_id -> item data
items: Dict[int, Item] = {}
next_id = 1


@app.get("/items")
def list_items():
    return [{"id": item_id, **item.dict()} for item_id, item in items.items()]


@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, **item.dict()}


@app.post("/items", status_code=201)
def create_item(item: Item):
    global next_id
    item_id = next_id
    items[item_id] = item
    next_id += 1
    return {"id": item_id, **item.dict()}


@app.put("/items/{item_id}")
def update_item(item_id: int, updated: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = updated
    return {"id": item_id, **updated.dict()}


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return None
