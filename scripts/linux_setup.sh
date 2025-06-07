#!/usr/bin/env bash
set -euo pipefail

if ! command -v zenity >/dev/null; then
    echo "zenity is required for installation" >&2
    exit 1
fi

INSTDIR=$(zenity --file-selection --directory --title="Select installation directory")
if [[ -z "$INSTDIR" ]]; then
    zenity --error --text="Installation cancelled"
    exit 1
fi

mkdir -p "$INSTDIR"
cp "$(dirname "$0")/ytm-neoplayer" "$INSTDIR/"
cat > "$HOME/.local/share/applications/ytm-neoplayer.desktop" <<EOM
[Desktop Entry]
Name=YT Music Player
Exec=$INSTDIR/ytm-neoplayer
Type=Application
Terminal=false
EOM
zenity --info --text="YT Music Player installed to $INSTDIR"
