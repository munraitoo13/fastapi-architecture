from fastapi import APIRouter

items_router = APIRouter(prefix="/items")

@items_router.get("/")
async def read_items():
    return [{"item_id": "Foo"}, {"item_id": "Bar"}]
