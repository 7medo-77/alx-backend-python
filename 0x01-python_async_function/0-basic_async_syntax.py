#!/usr/bin/env python3
"""
Module which returns a random number
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Async function returning a random number
    """
    rand_time: float = random.random() * max_delay
    await asyncio.sleep(rand_time)
    return rand_time
