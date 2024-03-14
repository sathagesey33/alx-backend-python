#!/usr/bin/env python3
"""
Module for calculating the length of elements in a list.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculates the length of elements in a list.

    Args:
        lst (Iterable[Sequence]): The input list of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple
        contains a sequence from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]


if __name__ == "__main__":
    print(element_length.__annotations__)
