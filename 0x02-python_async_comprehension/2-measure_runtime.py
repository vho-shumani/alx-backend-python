#!/usr/bin/env python3
"""2-measure_runtime.py"""
import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure the total runtime and return it
    """
    tasks = [async_comprehension() for _ in range(4)]
    start = time.time()
    await asyncio.gather(*tasks)
    end = time.time()
    return end - start

async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)