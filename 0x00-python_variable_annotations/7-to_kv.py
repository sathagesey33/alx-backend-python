#!/usr/bin/env python3
"""
Module for converting a string and int/float to a tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a string and int/float to a tuple.

    Args:
        k (str): The string value.
        v (Union[int, float]): The int or float value.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string k
        and the second element is the square of the int/float v.
    """
    return (k, v ** 2)


if __name__ == "__main__":
    print(to_kv.__annotations__)
    print(to_kv("eggs", 3))
    print(to_kv("school", 0.02))
