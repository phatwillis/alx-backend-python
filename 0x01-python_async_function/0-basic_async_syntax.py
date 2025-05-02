#!/usr/bin/env python3
""" learning async/await"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """an asynchronous coroutine that takes
    in an integer argument
    (max_delay, with a default value of 10)
     that waits for a random delay between 0
     and max_delay (included and float value)
     seconds and eventually returns it."""
    delay = random.uniform(1, float(max_delay))
    await asyncio.sleep(delay)
    return delay
