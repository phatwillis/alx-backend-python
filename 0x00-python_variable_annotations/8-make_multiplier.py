#!/usr/bin/env python3
"""returns a multiplier function"""

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """returns a multiplier function"""

    def actual_multiplier(multiplier_two: float) -> float:
        return multiplier_two * multiplier

    return actual_multiplier
