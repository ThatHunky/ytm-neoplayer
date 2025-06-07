#!/usr/bin/env bash
set -euo pipefail

pyinstaller --onefile --name ytm-neoplayer ytm_player/__main__.py

# Build a Windows installer with NSIS if available.
if command -v makensis >/dev/null; then
    makensis scripts/installer.nsi
fi

# Build a macOS DMG if running on macOS
if [[ "$(uname)" == "Darwin" ]]; then
    bash scripts/macos_dmg.sh
fi

# Build a Linux .run installer if running on Linux and makeself is installed
if [[ "$(uname)" == "Linux" ]] && command -v makeself >/dev/null; then
    bash scripts/linux_installer.sh
fi
