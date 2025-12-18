"""
Temperature measurement CLI.

Converts temperatures between Celsius, Fahrenheit, and Kelvin.

Usage examples:
    python script.py --value 100 --from C --to F
    python script.py -v 273.15 -f K -t C
    python script.py -v 32 -f fahrenheit -t celsius
"""

import argparse
import sys

import temperature as temp


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert temperatures between Celsius (C), Fahrenheit (F), and Kelvin (K)."
    )
    parser.add_argument(
        "-v",
        "--value",
        required=True,
        type=float,
        help="Numeric temperature value in the source unit.",
    )
    parser.add_argument(
        "-f",
        "--from",
        dest="from_unit",
        required=True,
        help="Source unit (C/F/K or full names like celsius, fahrenheit, kelvin).",
    )
    parser.add_argument(
        "-t",
        "--to",
        dest="to_unit",
        required=True,
        help="Destination unit (C/F/K or full names).",
    )
    return parser


def main(argv=None) -> int:
    if argv is None:
        argv = sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        src = temp.normalize_unit(args.from_unit)
        dst = temp.normalize_unit(args.to_unit)
        result = temp.convert(args.value, src, dst)
        print(temp.format_value(result, dst))
        return 0
    except ValueError as e:
        print(str(e), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
