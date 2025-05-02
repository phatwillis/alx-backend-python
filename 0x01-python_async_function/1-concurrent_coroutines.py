#!/usr/bin/env python3
""" learning async/await"""
import asyncio

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ will spawn wait_random n times with the
    specified max_delay"""

    # used asyncio.gather with a variable number *arg
    # gets the wait_random result and appends to list
    wait_times = await asyncio.gather(
        *[wait_random(max_delay) for _ in range(n)]
    )
    return sorted(wait_times)
