#!/usr/bin/env python3
"""
Module which includes a function that returns
an array of sorted float numbers
"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Async function returning an
    array of sorted float numbers
    """
    arrayFloat: List[float] = []

    for _ in range(n):
        arrayFloat.append(await wait_random(max_delay))

    return sorted(arrayFloat)
