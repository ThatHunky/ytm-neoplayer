"""Main application window."""

from __future__ import annotations

from pathlib import Path

from PySide6.QtWidgets import QMainWindow  # type: ignore

import webview  # type: ignore


class MainWindow(QMainWindow):
    """Top-level window embedding a webview."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("YT Music Player")
        html = Path(__file__).resolve().parents[1] / "web" / "player.html"
        self._view = webview.create_window("Player", html.as_uri())
