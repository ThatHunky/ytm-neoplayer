from ytm_player.models import Track
from ytm_player.player import Player


def test_playlist_navigation() -> None:
    player = Player()
    player.enqueue(Track(id="1", title="one"))
    player.enqueue(Track(id="2", title="two"))

    assert player.current().id == "1"
    assert player.next().id == "2"
    assert player.previous().id == "1"
    assert player.previous() is None
    assert player.next().id == "2"
    assert player.next() is None


def test_clear() -> None:
    player = Player()
    player.enqueue(Track(id="1", title="one"))
    player.clear()
    assert player.current() is None
    assert player.playlist.tracks == []
