from fastapi import APIRouter
from app.items.models import Item
from app.items.services import list_items, get_item, add_item, remove_item

items_router = APIRouter(prefix="/items")


@items_router.get("/")
async def read_items():
    """Fetch and return a list of all items."""

    return list_items()


@items_router.get("/{item_name}")
async def read_item(item_name: str):
    """Fetch and return an item by its name."""

    item = get_item(item_name)
    if item:
        return item

    return {"error": "Item not found"}


@items_router.post("/")
async def create_item(item: Item):
    """Creates a new item and returns the created item."""

    added_item = add_item(item)

    return added_item


@items_router.delete("/{item_name}")
async def delete_item(item_name: str):
    """Deletes an item by its name."""

    success = remove_item(item_name)
    if success:
        return {"message": "Item deleted"}

    return {"error": "Item not found"}
