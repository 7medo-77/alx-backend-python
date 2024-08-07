#!/usr/bin/env python3
"""
Module which defines a
funciton that returns a task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    Function that returns a future-like object
    """
    # return asyncio.create_task(wait_random(max_delay))
    return asyncio.Task(wait_random(max_delay))
