"""Main module"""
from src.pi import approx_pi
from src.verify import correct_decimal_points

from src.cli import collect
from src.helpers import can_convert

ARGS = collect({
    "iterations": {
        "text": """Iterations (>= 1) of the approximation algorithm
(corresponds to a polygon with (2 ** n) * 3 corners):""",
        "required": True,
        "check": lambda x: can_convert(x, int) and int(x) > 0,
        "transform": int
    },
    "precision": {
        "text": "Precision used for approximation (default is iterations * 4):",
        "required": False,
        "check": lambda x: can_convert(x, int),
        "transform": lambda x: int(x) if x else None
    }
})

print("Approximating pi...")

pi = approx_pi(ARGS["iterations"], ARGS["precision"])

correct = correct_decimal_points(pi)

print("Approximated pi to", pi)
print("Calculated", correct, "correct decimal point{}".format(
    "s" if correct > 1 else ""))
