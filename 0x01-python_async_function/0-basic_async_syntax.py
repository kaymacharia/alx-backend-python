#!/usr/bin/env python3
'''Task 0 '''
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay
    """
    wait = random.random() * max_delay  # Generate a random float between 0 and max_delay
    await asyncio.sleep(wait)  # Wait for the delay
    return wait  # Return the delay time
