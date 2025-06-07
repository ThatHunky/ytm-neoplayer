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

To build a local installer run:

```bash
make installer
```

If `makensis` is available on your system, this will also produce a Windows GUI
installer using NSIS. On macOS a `.dmg` will be created and on Linux a
self-extracting `.run` installer is produced when `makeself` is installed.
