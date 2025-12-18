import sys
import subprocess
from pathlib import Path


def run_cli(args):
    script = Path(__file__).resolve().parents[1] / "script.py"
    cmd = [sys.executable, str(script)] + args
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def test_cli_converts_c_to_f():
    code, out, err = run_cli(["--value", "100", "--from", "C", "--to", "F"])
    assert code == 0
    assert out == "212.00 F"
    assert err == ""


def test_cli_accepts_full_names_case_insensitive():
    code, out, _ = run_cli(["-v", "273.15", "-f", "kelvin", "-t", "celsius"])
    assert code == 0
    assert out == "0.00 C"


def test_cli_rejects_below_absolute_zero():
    code, out, err = run_cli(["-v", "-500", "-f", "F", "-t", "C"])
    assert code != 0
    assert "absolute zero" in err.lower()
    assert out == ""
