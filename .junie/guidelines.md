# Project Development Guidelines

This document captures project-specific know-how to speed up onboarding and day-to-day work for advanced contributors.

Repository root: `/Users/abhisheksaxena/PyCharmMiscProject`


## Build / Configuration

- Python: The project is pure-Python and has no third-party runtime dependencies for core features. It targets CPython 3.9+ (tested locally on Python 3.11).
- Virtual environment: optional but recommended.
  - Create: `python -m venv .venv && source .venv/bin/activate`
  - Upgrade pip: `python -m pip install -U pip`
- No packaging/entry-points are defined; invoke modules directly with `python`.

CLI entry point
- The CLI is implemented in `script.py` and uses `argparse`. Run it as follows:
  - `python script.py --value 100 --from C --to F` → `212.00 F`
  - `python script.py -v 273.15 -f kelvin -t celsius` → `0.00 C`
  - On invalid inputs (e.g., below absolute zero), it exits non‑zero and writes an error to stderr.


## Testing

There are two complementary testing approaches: `pytest` (preferred) and the standard library `unittest`. The repository contains pytest-style tests already. If `pytest` is unavailable, you can still validate behavior using `unittest` or by exercising the CLI.

Pytest (preferred)
- Install: `python -m pip install pytest`
- Run all tests: `pytest -q`
- Run a single file: `pytest -q tests/test_temperature.py -q`
- Notes:
  - `tests/test_temperature.py` covers conversion math, unit normalization, absolute-zero validation, and formatting.
  - `tests/test_script_cli.py` performs black-box CLI tests by spawning a Python subprocess; it assumes `python script.py` is runnable from repo root.

Standard library unittest (no external deps)
- You can run targeted tests using unittest when `pytest` is not installed.
- Example commands verified locally:
  - Run a single unittest file: `python -m unittest -q tests/test_unittest_demo.py`
  - Discover tests (pattern-based): `python -m unittest -q discover -s tests -p 'test_*.py'`
- Demo test used for verification (removed after demonstration):
  - `tests/test_unittest_demo.py` contained two tests: a C→F conversion happy path and an absolute-zero error case. It ran successfully (`OK`). It has been deleted to keep the repo clean as per the task’s requirements.

Adding tests
- For pytest:
  - Place files under `tests/` with names matching `test_*.py`.
  - Use `pytest.mark.parametrize` for conversion matrices; prefer `math.isclose` with tight tolerances for float comparisons.
  - CLI tests should call a helper like `subprocess.run([sys.executable, 'script.py', ...])` and assert on `returncode`, `stdout`, `stderr`.
- For unittest:
  - Derive from `unittest.TestCase`, use `assertAlmostEqual` for floating point; prefer `places>=9` for stability.
  - Keep CLI subprocess helpers minimal and assert both exit code and streams.

Continuous verification tips
- When `pytest` is not available, minimally validate with:
  - `python script.py --value 100 --from C --to F` → `212.00 F`
  - `python script.py -v 273.15 -f kelvin -t celsius` → `0.00 C`
  - `python script.py -v -500 -f F -t C` should emit an absolute-zero error to stderr and exit with code 1.


## Additional Development Notes

Module boundaries
- `temperature.py` is the core domain module. Keep all temperature math, unit normalization, and constraints here. Public API:
  - `normalize_unit(str) -> Literal['C','F','K']`
  - `validate_physical(float, Unit) -> None`
  - `to_celsius(float, Unit) -> float`, `from_celsius(float, Unit) -> float`
  - `convert(float, from_unit: str, to_unit: str) -> float`
  - `format_value(float, Unit) -> str`
- `script.py` is a thin CLI over `temperature.py`, handling parsing, error reporting, and stdout/stderr separation. Do not duplicate conversion logic here.

Units and normalization
- `normalize_unit` accepts symbols and case-insensitive full names: `c/C/celsius/Celsius`, `f/fahrenheit`, `k/kelvin`. It raises `ValueError` on unsupported units.

Physical constraints
- Absolute zero is enforced per-unit. All conversion paths validate before computing to avoid propagating invalid states.

Error handling & UX
- CLI prints results to stdout and errors to stderr, exiting with `0` on success and `1` on validation errors. This contract is what CLI tests assert against; keep it stable.

Floating-point behavior
- Conversions use straightforward formulas. Tests use `math.isclose`/`assertAlmostEqual` with tight tolerances to avoid flaky comparisons.
- Human-facing formatting defaults to two decimals via `format_value(value, unit)`.

Type hints
- The API leverages `typing.Literal` for temperature units. Keep annotations precise; they help IDEs and static analysis.

Code style
- Follow the existing style: explicit functions, small helpers, conventional naming, and docstrings for public functions. Avoid inline comments unless clarifying non-obvious decisions.

Extending functionality
- If you add new units or scales, extend `normalize_unit` mapping and add conversion routes through Celsius; update absolute-zero constants and tests accordingly.
- For packaging or distribution, consider exposing a console script entry-point wrapping `script.main`.
