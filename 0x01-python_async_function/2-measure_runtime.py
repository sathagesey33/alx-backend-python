#!/usr/bin/env python3
""" measure the runtime """
from typing import Callable
from time import perf_counter
from asyncio import run
from 1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time
    for wait_n(n, max_delay) and returns total_time / n.

    Args:
        n: Number of times to call wait_n.
        max_delay: Maximum delay for wait_n.

    Returns:
        float: Average execution time per call.
    """
    start_time = perf_counter()
    run(wait_n(n, max_delay))
    end_time = perf_counter()
    total_time = end_time - start_time
    return total_time / n


if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
