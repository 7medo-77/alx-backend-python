#!/usr/bin/env python3
import asyncio
import random 

async def wait_random(max_delay=10):
    await asyncio.sleep(random.uniform(0, max_delay))
    return max_delay
