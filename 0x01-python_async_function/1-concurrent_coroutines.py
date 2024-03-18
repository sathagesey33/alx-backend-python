#!/usr/bin/env python3
""" write an async routine called wait_n """
import asyncio
from typing import List
from random import uniform, seed
from time import perf_counter

seed(1)  # Set a seed for the random module for reproducible results


async def wait_random(max_delay: int) -> float:
    """
    Asynchronous coroutine that waits
    for a random delay between 0 and max_delay seconds.

    Args:
        max_delay: Maximum delay in seconds.

    Returns:
        float: The random delay that was waited for.
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random
    n times with the specified max_delay.

    Args:
        n: Number of times to spawn wait_random.
        max_delay: Maximum delay in seconds.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    start_time = perf_counter()
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    end_time = perf_counter()
    print(f"Total time taken: {end_time - start_time:.2f} seconds.")
    return sorted(delays)
