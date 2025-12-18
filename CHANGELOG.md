# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog, and this project adheres to Semantic Versioning.

## [Unreleased]

## [0.0.2] - 2025-12-08
### Added
- Temperature conversion CLI (`script.py`) using argparse with `--value/-v`, `--from/-f`, and `--to/-t` options.
- Unit normalization accepting symbols and full names (e.g., `c/C/celsius`, `f/fahrenheit`, `k/kelvin`).
- Absolute-zero validation for C/F/K to prevent physically impossible inputs.
- Human-friendly formatting of results to two decimals via `format_value`.

### Tests
- Pytest coverage for conversion math, unit normalization, absolute-zero validation, and CLI behavior.

### Notes
- Git metadata was not available in this environment, so changes were inferred from the current codebase rather than commit history. Semantic version increment defaults to a patch release.

## [0.0.1] - 2025-12-08
### Added
- Initialize changelog structure using Keep a Changelog.

### Notes
- Could not extract the last commits because Git metadata was not available in this environment at generation time; defaulted to a patch release. Re-run the generator within the repository to populate user-facing changes from the latest 2–5 commits.
