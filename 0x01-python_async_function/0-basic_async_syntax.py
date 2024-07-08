#!/usr/bin/env python3
import random
import asyncio
"""0-basic_async_syntax.py"""


async def wait_random(max_delay: int = 10):
    """waits for a random delay between 0 and max_delay
    seconds and eventually returns it.

    args:
        max_delay(int): the maximum time in sec to delay.

    return:
        the dealay time
    """
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
