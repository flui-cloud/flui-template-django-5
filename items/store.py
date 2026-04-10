"""In-memory item store. Resets on every server restart."""

from datetime import datetime, timezone
from typing import Optional

_items: dict[str, dict] = {}


def _seed() -> None:
    if _items:
        return
    now = datetime.now(timezone.utc).isoformat()
    _items['1'] = {
        'id': '1',
        'name': 'Welcome to Flui',
        'description': 'Your first demo item — feel free to delete it.',
        'createdAt': now,
    }
    _items['2'] = {
        'id': '2',
        'name': 'Try the API',
        'description': 'Visit /docs to explore the OpenAPI documentation.',
        'createdAt': now,
    }


_seed()


def list_items() -> list[dict]:
    return sorted(_items.values(), key=lambda i: i['createdAt'], reverse=True)


def get_item(item_id: str) -> Optional[dict]:
    return _items.get(item_id)


def create_item(name: str, description: str) -> dict:
    new_id = str(int(datetime.now(timezone.utc).timestamp() * 1000))
    item = {
        'id': new_id,
        'name': name,
        'description': description,
        'createdAt': datetime.now(timezone.utc).isoformat(),
    }
    _items[new_id] = item
    return item


def delete_item(item_id: str) -> bool:
    return _items.pop(item_id, None) is not None
