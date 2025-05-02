#!/usr/bin/env python3
"""an async generator"""
import asyncio
import random

from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async generator that yields random numbers
     using a Generator type hint is because it returns
     a Python generator object which is an iterable"""
    for _ in range(10):
        await asyncio.sleep(1)
        num = random.uniform(0, 10)
        yield num
