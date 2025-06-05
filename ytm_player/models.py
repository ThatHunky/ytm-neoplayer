"""Domain models."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass(slots=True)
class Track:
    """A playable track."""

    id: str
    title: str


@dataclass(slots=True)
class Playlist:
    """Queue of tracks."""

    tracks: List[Track] = field(default_factory=list)
