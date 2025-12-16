from app.items.models import Item
from app.database.database import items_db


def fetch_all() -> list[Item]:
    """Fetch all items from the database."""

    return list(items_db)


def insert(item: Item) -> Item:
    """Insert a new item into the database."""

    items_db.append(item)

    return item


def fetch_by_name(name: str) -> Item | None:
    """Fetch an item by its name from the database."""

    for item in items_db:
        if item.name == name:
            return item

    return None


def delete_by_name(name: str) -> bool:
    """Delete an item by its name from the database."""

    initial_len = len(items_db)

    items_db[:] = [item for item in items_db if item.name != name]

    if len(items_db) == initial_len:
        return False

    return True
