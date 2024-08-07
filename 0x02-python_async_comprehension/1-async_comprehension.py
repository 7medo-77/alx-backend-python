#!/usr/bin/env python3
"""
Module containing generator yielding
random number for 10 iterations
"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Function iterating over imported generator
    """
    return [rand async for rand in async_generator()]
