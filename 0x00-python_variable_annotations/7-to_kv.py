#!/usr/bin/env python3
"""a type-annotated function to_kv that takes a
string k and an int OR float v as arguments and
returns a tuple."""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """returns a key value tuple"""
    square_of_v: float = (v ** 2)
    return k, square_of_v
