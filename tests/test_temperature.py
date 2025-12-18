import math
import pytest

import temperature as temp


@pytest.mark.parametrize(
    "value, src, dst, expected",
    [
        (0, "C", "F", 32.0),
        (100, "C", "F", 212.0),
        (32, "F", "C", 0.0),
        (212, "F", "C", 100.0),
        (0, "C", "K", 273.15),
        (273.15, "K", "C", 0.0),
        (255.3722222222222, "K", "F", 0.0),
        ("100", "celsius", "fahrenheit", 212.0),  # type: ignore[arg-type]
    ],
)
def test_convert_between_units(value, src, dst, expected):
    # Ensure the function can handle str-like numbers via float casting at call site
    v = float(value)
    assert math.isclose(temp.convert(v, src, dst), expected, rel_tol=1e-12, abs_tol=1e-12)


@pytest.mark.parametrize(
    "bad_unit",
    ["X", "deg", "cel", "rankine", ""],
)
def test_normalize_unit_rejects_bad_units(bad_unit):
    with pytest.raises(ValueError):
        temp.normalize_unit(bad_unit)


@pytest.mark.parametrize(
    "value, unit",
    [
        (temp.ABSOLUTE_ZERO_C - 1e-9, "C"),
        (temp.ABSOLUTE_ZERO_F - 1e-9, "F"),
        (temp.ABSOLUTE_ZERO_K - 1e-9, "K"),
    ],
)
def test_validate_physical_below_absolute_zero_raises(value, unit):
    with pytest.raises(ValueError):
        temp.validate_physical(value, unit)  # type: ignore[arg-type]


def test_format_value_rounding_and_unit():
    assert temp.format_value(36.6666, "C") == "36.67 C"
    assert temp.format_value(0, "K") == "0.00 K"
