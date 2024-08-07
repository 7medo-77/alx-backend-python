#!/usr/bin/env python3
"""
Module which includes a function that returns
an array of sorted float numbers
"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Async function returning an
    array of sorted float numbers
    """
    arrayFloat: List[float] = []

    for _ in range(n):
        arrayFloat.append(await task_wait_random(max_delay))

    return sorted(arrayFloat)
