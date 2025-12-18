# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A collection of Python utilities including a temperature conversion CLI, a scientific calculator, and a rock-paper-scissors game. Pure Python with no runtime dependencies.

## Commands

**Run temperature CLI:**
```bash
python script.py --value 100 --from C --to F    # Output: 212.00 F
python script.py -v 273.15 -f kelvin -t celsius # Output: 0.00 C
```

**Run tests:**
```bash
pytest -q                              # Run all tests
pytest -q tests/test_temperature.py   # Run single file
```

**Without pytest:**
```bash
python -m unittest discover -s tests -p 'test_*.py'
```

## Architecture

### Temperature Conversion (main feature)
- `temperature.py` - Core domain module with conversion logic, unit normalization, and absolute-zero validation. All conversions route through Celsius as the intermediate unit.
- `script.py` - CLI wrapper using argparse. Outputs results to stdout, errors to stderr. Exit code 0 on success, 1 on validation errors.

### Key APIs in temperature.py
- `normalize_unit(str)` - Accepts symbols (C/F/K) or full names (celsius/fahrenheit/kelvin), case-insensitive
- `convert(value, from_unit, to_unit)` - Main conversion function
- `validate_physical(value, unit)` - Enforces absolute zero constraints
- `format_value(value, unit)` - Formats to 2 decimal places with unit

### Other Scripts
- `hello.py` - Interactive scientific calculator with memory, history, and trig functions
- `rock_paper_scissors.py` - CLI game with score tracking

## Testing Conventions

- Tests live in `tests/` with `test_*.py` naming
- Use `pytest.mark.parametrize` for conversion matrices
- Use `math.isclose` with tight tolerances for float comparisons
- CLI tests spawn subprocess and assert on returncode/stdout/stderr
