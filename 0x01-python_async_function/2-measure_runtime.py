#!/usr/bin/env python3
"""2-measure_runtime.py"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n
    Args:
    n(int): number of time wait_random is spawn
    max_delat(int): maximum delay time in sec
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    return (end_time - start_time) / n
