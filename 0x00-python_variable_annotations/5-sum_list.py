#!/usr/bin/env python3
"""returns sum of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum list func"""
    sumoffloats: float = 0
    for f in input_list:
        sumoffloats += f
    return sumoffloats
