#!/usr/bin/env python3
"""
Async Generator

This module contains a coroutine called async_generator that loops 10 times,
each time asynchronously waiting 1 second,
then yielding a random number between 0 and 10.
"""

import asyncio
import random


async def async_generator() -> float:
    """
    Coroutine that generates random numbers asynchronously.

    This coroutine loops 10 times, each time asynchronously waiting 1 second,
    then yielding a random number between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


# Testing the async_generator coroutine
async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

if __name__ == "__main__":
    asyncio.run(print_yielded_values())
