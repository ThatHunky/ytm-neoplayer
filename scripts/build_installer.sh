#!/usr/bin/env bash
set -euo pipefail

pyinstaller --onefile --name ytm-neoplayer ytm_player/__main__.py
