# Changelog

## 1.0.4 - 2025-06-07

- Install cosign via official GitHub Action for reliable SBOM signing.

## 1.0.3 - 2025-06-07

- Install `cyclonedx-py` and `cosign` in CI workflow for SBOM generation.

## 1.0.2 - 2025-06-07

- Install `pytest` in CI workflow to enable tests.

## 1.0.1 - 2025-06-06

- Added self-improvement instructions and versioning rules to AGENTS.md.
- Fixed build workflow by using `uv pip --system` and installing `ruff` in CI.



## 1.0.0 - 2025-06-06


- Initial public release.
- Adds basic player UI using PySide6 and pywebview.
- Bundles the app as a standalone binary with PyInstaller.
