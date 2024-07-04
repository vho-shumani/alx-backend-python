#!/usr/bin/env python3
"""8-make_multiplier.py"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a tuple"""
    def multiply(n: float) -> float:
        n * multiplier
    return multiply
