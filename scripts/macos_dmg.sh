#!/usr/bin/env bash
set -euo pipefail

WORKDIR=$(mktemp -d)
cp dist/ytm-neoplayer "$WORKDIR/ytm-neoplayer"
cat > "$WORKDIR/README.txt" <<EOM
Drag ytm-neoplayer to Applications to install.
EOM
hdiutil create ytm-neoplayer.dmg -volname "YT Music Player" -srcfolder "$WORKDIR" -ov
rm -rf "$WORKDIR"
