#!/usr/bin/env python3
"""returns an asyncio.task"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """regular function that creates an asyncio task
    for wait_random"""
    created_task = asyncio.create_task(wait_random(max_delay))
    return created_task
