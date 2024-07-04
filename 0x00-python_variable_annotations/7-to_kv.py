#!/usr/bin/env python3
"""7-to_kv.py"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple"""
    return (k, v**2)
