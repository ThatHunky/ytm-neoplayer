"""Application entry point."""

from __future__ import annotations

import sys
from PySide6.QtWidgets import QApplication  # type: ignore

from ytm_player.ui.main_window import MainWindow


def main() -> None:
    """Launch the Qt application."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":  # pragma: no cover - CLI entry
    main()
