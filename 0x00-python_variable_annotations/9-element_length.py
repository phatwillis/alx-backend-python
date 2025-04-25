#!/usr/bin/env python3
"""fixing annotation"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) \
        -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """I only fixed the annotations"""
    return [(i, len(i)) for i in lst]
