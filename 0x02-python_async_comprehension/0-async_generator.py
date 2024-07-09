#!/usr/bin/env python3
"""0-async_generator.py"""
import asyncio
from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """loop 10 times, then yield a random number between 0 and 10"""
    for i in range(10):
        await asyncio.sleep(0.1)
        yield random.uniform(0, 10)
