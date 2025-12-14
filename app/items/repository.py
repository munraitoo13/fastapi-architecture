from models import Item

# database operations
def get_all_items():
	return items_db

def create_item(item: Item):
	items_db.append(item)
	return item

def get_item_by_name(name: str):
	for item in items_db:
		if item.name == name:
			return item
	return None

def delete_item(name: str):
	global items_db
	items_db = [item for item in items_db if item.name != name]

# local storage for demonstration purposes
items_db = []
