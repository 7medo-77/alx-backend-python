#!/usr/bin/env python3
"""

"""
import asyncio, random, time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int = 10) -> float:
    """

    """
    startTime = time.perf_counter()
    await wait_n(n, max_delay)
    endTime = time.perf_counter() - startTime
    return endTime / n
