# ytm-neoplayer

Minimal YouTube Music desktop player built with PySide6 and pywebview. All
playback occurs via the official YouTube IFrame Player API.

## Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
yt-music-player
```

## Testing

```bash
pip install -e .
pip install ruff black mypy pytest
ruff check .
ruff format --check .
pytest -q
```

## Installer Builds

Tagged releases trigger a GitHub Actions workflow that bundles the application with PyInstaller. Pre-built binaries for Windows, macOS and Linux can be downloaded from the workflow run artifacts.
