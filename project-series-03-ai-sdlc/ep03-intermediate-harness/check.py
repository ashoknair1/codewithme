"""check.py — the local harness gate for MiniCRM (Ep 3).

Run before calling anything done:  python check.py
Exit code 0 = the harness is green. Anything else = not done, whatever
the agent says. Deliberately boring: compile everything, run the tests.
"""
import subprocess
import sys

STEPS = [
    ("compile", [sys.executable, "-m", "compileall", "-q", "../project"]),
    ("tests", [sys.executable, "-m", "pytest", "-q", "../project/tests"]),
]

for name, cmd in STEPS:
    print(f"== {name}: {' '.join(cmd)}")
    if subprocess.run(cmd).returncode != 0:
        print(f"HARNESS RED at step: {name}")
        sys.exit(1)

print("HARNESS GREEN — safe to call it done.")
