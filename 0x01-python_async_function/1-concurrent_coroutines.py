#!/usr/bin/env python3
"""1-concurrent_coroutines.py"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return list of all the delays in ascending order
    args:
    n(int): number of time wait_random is spawn
    max_delat(int): maximum delay time in sec
    """
    tasks_list = [wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks_list)]
