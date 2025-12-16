from app.items.models import Item
from app.items.repository import (
    insert,
    delete_by_name,
    fetch_all,
    fetch_by_name,
)


def list_items() -> list[Item]:
    """Fetches and return a list of all items."""

    items = fetch_all()

    return items


def get_item(name: str) -> Item | None:
    """Fetches and return an item by name."""

    item = fetch_by_name(name)

    return item


def add_item(item: Item) -> Item:
    """Inserts a new item into the database."""

    created_item = insert(item)

    return created_item


def remove_item(name: str) -> bool:
    """Deletes an item by their name."""

    success = delete_by_name(name)

    return success
