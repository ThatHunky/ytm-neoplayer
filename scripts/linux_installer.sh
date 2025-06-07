#!/usr/bin/env bash
set -euo pipefail

# Prepare directory for makeself package
PKGDIR=$(mktemp -d)
cp dist/ytm-neoplayer "$PKGDIR/ytm-neoplayer"
cp scripts/linux_setup.sh "$PKGDIR/install.sh"
chmod +x "$PKGDIR/install.sh"
makeself --nox11 "$PKGDIR" ytm-neoplayer-installer.run "YT Music Player Installer" ./install.sh
rm -rf "$PKGDIR"
