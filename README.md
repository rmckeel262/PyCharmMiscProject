# PyCharmMiscProject

[![Tests](https://github.com/rmckeel262/PyCharmMiscProject/actions/workflows/tests.yml/badge.svg)](https://github.com/rmckeel262/PyCharmMiscProject/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/rmckeel262/PyCharmMiscProject/branch/main/graph/badge.svg)](https://codecov.io/gh/rmckeel262/PyCharmMiscProject)

A collection of Python and Java utilities including a temperature conversion CLI, scientific calculator, and rock-paper-scissors game.

## Features

### Temperature Converter CLI
Convert temperatures between Celsius, Fahrenheit, and Kelvin with absolute zero validation.

```bash
python script.py --value 100 --from C --to F    # Output: 212.00 F
python script.py -v 273.15 -f kelvin -t celsius # Output: 0.00 C
```

### Scientific Calculator
Interactive calculator with:
- Basic arithmetic (+, -, *, /, **, %)
- Trigonometric functions (sin, cos, tan, etc.)
- Logarithmic functions (log, ln)
- Memory operations (store, recall, clear)
- Calculation history

```bash
python hello.py
```

### Rock Paper Scissors
Classic game with score tracking. Available in Python and Java.

**Python:**
```bash
python rock_paper_scissors.py
```

**Java:**
```bash
javac RockPaperScissors.java
java RockPaperScissors
```

## Requirements

- Python 3.9+
- No runtime dependencies for core features
- pytest (optional, for running tests)

## Installation

```bash
git clone https://github.com/rmckeel262/PyCharmMiscProject.git
cd PyCharmMiscProject
python -m venv .venv && source .venv/bin/activate
pip install pytest  # optional, for tests
```

## Running Tests

```bash
pytest -v
```

## License

MIT
