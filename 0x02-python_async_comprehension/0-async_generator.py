#!/usr/bin/env python
"""
Module containing generator yielding
random number for 10 iterations
"""
import asyncio
import random


async def async_generator():
    """
    Generator yielding random number for 10 iterations
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
