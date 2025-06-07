# Changelog

## 1.0.5 - 2025-06-07

- Fix SBOM generation command in workflows and documentation.
- Update AGENTS guide edition date.

## 1.0.4 - 2025-06-07

- Install `cyclonedx-bom` in workflows to ensure SBOM generation succeeds.

## 1.0.3 - 2025-06-07

- Install `pytest` in CI so tests run properly.

## 1.0.2 - 2025-06-07

- Fix release workflow by installing `cosign` via dedicated action.

## 1.0.1 - 2025-06-06

- Added self-improvement instructions and versioning rules to AGENTS.md.
- Fixed build workflow by using `uv pip --system` and installing `ruff` in CI.



## 1.0.0 - 2025-06-06


- Initial public release.
- Adds basic player UI using PySide6 and pywebview.
- Bundles the app as a standalone binary with PyInstaller.
