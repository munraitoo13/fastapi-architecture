from pydantic import BaseModel

# model for item
class Item(BaseModel):
	name: str
	amount: int
