from __future__ import annotations

from typing import Any

import pytest

import ytm_player.yt_api as yt


class FakeList:
    def __init__(self, items: list[dict[str, Any]]) -> None:
        self._items = items

    def execute(self) -> dict[str, Any]:
        return {"items": self._items}


class FakeSearch:
    def __init__(self, items: list[dict[str, Any]]) -> None:
        self._items = items

    def list(self, *args: Any, **kwargs: Any) -> FakeList:
        return FakeList(self._items)


class FakeService:
    def __init__(self, items: list[dict[str, Any]]) -> None:
        self._items = items

    def search(self) -> FakeSearch:
        return FakeSearch(self._items)


def test_search(monkeypatch: pytest.MonkeyPatch) -> None:
    items = [{"id": {"videoId": "123"}}]
    monkeypatch.setattr(yt, "build", lambda *a, **k: FakeService(items))
    res = yt.search("token", "query")
    assert res == ["123"]
