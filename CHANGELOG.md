# Changelog

## 1.0.11 - 2025-06-08

- Clarify Windows installer script path for PyInstaller output.

## 1.0.10 - 2025-06-07

- Fix Windows NSIS installer path to the built executable.

## 1.0.9 - 2025-06-07

- Add GUI installers for macOS (DMG) and Linux (makeself).

## 1.0.8 - 2025-06-07

- Add NSIS script to build a Windows GUI installer.

## 1.0.7 - 2025-06-09

- Fix PyInstaller entrypoint to allow running packaged binary.

## 1.0.6 - 2025-06-08

- Use `cosign sign-blob` to sign SBOM and update docs.
- Bump guide edition date.

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
