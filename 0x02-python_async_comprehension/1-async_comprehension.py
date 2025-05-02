#!/usr/bin/env python3
"""async comprehension"""
import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """function that performs async comprehension"""
    result_list = [i async for i in async_generator()]
    return result_list
