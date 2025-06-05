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
