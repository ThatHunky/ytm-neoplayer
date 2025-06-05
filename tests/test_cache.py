from ytm_player.cache import LRU


def test_lru_eviction() -> None:
    cache = LRU(2)
    cache.set("a", 1)
    cache.set("b", 2)
    cache.set("c", 3)
    assert cache.get("a") is None
    assert cache.get("b") == 2
