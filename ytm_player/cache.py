"""Tiny LRU cache implementation."""

from __future__ import annotations

from collections import OrderedDict
from typing import Any


class LRU:
    """Simple least-recently-used cache."""

    def __init__(self, size: int) -> None:
        self.size = size
        self._data: OrderedDict[Any, Any] = OrderedDict()

    def get(self, key: Any) -> Any:
        """Return cached value or ``None``."""
        if key in self._data:
            self._data.move_to_end(key)
            return self._data[key]
        return None

    def set(self, key: Any, value: Any) -> None:
        """Store ``value`` under ``key``."""
        if key in self._data:
            self._data.move_to_end(key)
        self._data[key] = value
        if len(self._data) > self.size:
            self._data.popitem(last=False)
