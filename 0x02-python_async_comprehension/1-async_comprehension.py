#!/usr/bin/env python3
"""
Module containing function which returns
list of random numbers from imported generator
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
