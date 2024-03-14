#!/usr/bin/env python3
"""
Module for adding two floats.
"""


def add(a: float, b: float) -> float:
    """
    Adds two floats.

    Args:
        a (float): The first float.
        b (float): The second float.

    Returns:
        float: The sum of a and b.
    """
    return a + b


if __name__ == "__main__":
    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__)
