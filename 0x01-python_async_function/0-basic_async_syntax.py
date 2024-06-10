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
    delay = random.uniform(0, max_delay)  # Generate a random float between 0 and max_delay
    await asyncio.sleep(delay)  # Wait for the delay
    return delay  # Return the delay time

# Example of how to run the coroutine
if __name__ == "__main__":
    # Run the coroutine and print the result
    delay = asyncio.run(wait_random(10))
    print(f"Waited for {delay} seconds")

