#!/usr/bin/env python3
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay time in seconds. Default is 10 seconds.

    Returns:
        float: The actual delay time in seconds.
    """
    wait = random.random(0, max_delay)  # Generate a random float between 0 and max_delay
    await asyncio.sleep(wait)  # Wait for the delay
    return wait  # Return the delay time
