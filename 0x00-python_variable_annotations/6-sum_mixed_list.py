#!/usr/bin/env python3
"""
Module for summing a mixed list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a mixed list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The input mixed list of integers and floats.

    Returns:
        float: The sum of the input mixed list of integers and floats.
    """
    return sum(mxd_lst)


if __name__ == "__main__":
    mixed = [5, 4, 3.14, 666, 0.99]
    ans = sum_mixed_list(mixed)
    print(ans == sum(mixed))
    print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))