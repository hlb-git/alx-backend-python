#!/usr/bin/env python3
"""Multiplies a float by a multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiplies a float by multiplier
    Args:
        multiplier (float): The multiplier
    Returns:
        A function that multiplies a float by multiplier
    """

    def multiplier_func(number: float) -> float:
        """Multiplies a float by multiplier"""
        return multiplier * number

    return multiplier_func
