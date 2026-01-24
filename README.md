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

## How to subscribe to Cloudflare WARP+ Unlimited

Cloudflare’s WARP app offers a paid WARP+ Unlimited tier. To subscribe:
1. Install the Cloudflare WARP app from the official store (iOS App Store, Google Play, or the Cloudflare website for desktop).
2. Sign in with a Cloudflare account or create one when prompted.
3. Open the app settings and select **Account** → **Upgrade to WARP+** (wording may vary slightly).
4. Choose the **WARP+ Unlimited** option and complete the in-app purchase.
5. After payment succeeds, return to the main screen and toggle WARP to **Connected**. The status should show **WARP+** confirming the subscription.
