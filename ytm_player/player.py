"""In-memory playlist and playback management."""

from __future__ import annotations

from dataclasses import dataclass, field

from .models import Playlist, Track


@dataclass
class Player:
    """Simple playlist-based player state."""

    playlist: Playlist = field(default_factory=Playlist)
    index: int = 0

    def current(self) -> Track | None:
        """Return the currently selected track."""
        if 0 <= self.index < len(self.playlist.tracks):
            return self.playlist.tracks[self.index]
        return None

    def enqueue(self, track: Track) -> None:
        """Append ``track`` to the playlist."""
        self.playlist.tracks.append(track)

    def next(self) -> Track | None:
        """Advance to the next track and return it."""
        if self.index + 1 < len(self.playlist.tracks):
            self.index += 1
            return self.playlist.tracks[self.index]
        return None

    def previous(self) -> Track | None:
        """Go back to the previous track and return it."""
        if self.index > 0:
            self.index -= 1
            return self.playlist.tracks[self.index]
        return None

    def clear(self) -> None:
        """Remove all tracks and reset position."""
        self.playlist.tracks.clear()
        self.index = 0
