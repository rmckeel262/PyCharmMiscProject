"""
Temperature conversion and validation utilities.

Supports conversions between Celsius (C), Fahrenheit (F), and Kelvin (K).
Includes absolute zero validation to prevent physically impossible values.

Example:
    from temperature import convert
    print(convert(100, 'C', 'F'))  # 212.0
"""
from typing import Literal

Unit = Literal['C', 'F', 'K']


ABSOLUTE_ZERO_C = -273.15
ABSOLUTE_ZERO_K = 0.0
ABSOLUTE_ZERO_F = -459.67


def normalize_unit(unit: str) -> Unit:
    """Normalize and validate unit strings.

    Accepts case-insensitive full names and symbols: 'c', 'C', 'celsius', 'Celsius', etc.
    Returns canonical one-letter units: 'C', 'F', or 'K'.
    Raises ValueError for unsupported units.
    """
    mapping = {
        'c': 'C', 'celsius': 'C', 'centigrade': 'C',
        'f': 'F', 'fahrenheit': 'F',
        'k': 'K', 'kelvin': 'K',
    }
    key = unit.strip().lower()
    if key not in mapping:
        raise ValueError(f"Unsupported temperature unit: {unit!r}. Use C, F, or K.")
    return mapping[key]  # type: ignore[return-value]


def validate_physical(value: float, unit: Unit) -> None:
    """Ensure the temperature is not below absolute zero for the given unit."""
    if unit == 'C' and value < ABSOLUTE_ZERO_C:
        raise ValueError(f"Temperature below absolute zero in Celsius: {value} < {ABSOLUTE_ZERO_C}")
    if unit == 'K' and value < ABSOLUTE_ZERO_K:
        raise ValueError(f"Temperature below absolute zero in Kelvin: {value} < {ABSOLUTE_ZERO_K}")
    if unit == 'F' and value < ABSOLUTE_ZERO_F:
        raise ValueError(f"Temperature below absolute zero in Fahrenheit: {value} < {ABSOLUTE_ZERO_F}")


# Base conversions through Celsius

def to_celsius(value: float, unit: Unit) -> float:
    validate_physical(value, unit)
    if unit == 'C':
        return value
    if unit == 'F':
        return (value - 32.0) * 5.0 / 9.0
    if unit == 'K':
        return value + ABSOLUTE_ZERO_C  # K to C
    raise AssertionError("Unreachable unit")


def from_celsius(value_c: float, unit: Unit) -> float:
    # validate input in Celsius relative to absolute zero before converting
    validate_physical(value_c, 'C')
    if unit == 'C':
        return value_c
    if unit == 'F':
        return value_c * 9.0 / 5.0 + 32.0
    if unit == 'K':
        return value_c - ABSOLUTE_ZERO_C  # C to K
    raise AssertionError("Unreachable unit")


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Convert temperature between units C, F, K.

    Args:
        value: numeric temperature value in the source unit.
        from_unit: source unit (C/F/K or full names).
        to_unit: destination unit (C/F/K or full names).

    Returns:
        Converted temperature value as float.
    """
    src = normalize_unit(from_unit)
    dst = normalize_unit(to_unit)
    c = to_celsius(value, src)
    out = from_celsius(c, dst)
    return float(out)


def format_value(value: float, unit: Unit) -> str:
    """Format temperature with unit symbol and reasonable precision."""
    # Use 2 decimal places by default
    return f"{value:.2f} {unit}"
