#!/usr/bin/env python3
"""
Module which exports a function
that returns time elapsed
"""
import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Function that returns time
    elapsed for a process
    """
    startTime = time.perf_counter()
    # await wait_n(n, max_delay)
    asyncio.run(wait_n(n, max_delay))
    endTime = time.perf_counter() - startTime
    return endTime / n
