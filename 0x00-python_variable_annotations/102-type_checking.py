#!/usr/bin/env python3
"""
module with type checking
"""


from typing import Tuple, List


def zoom_array(lst: List[int], factor: int = 2) -> Tuple[int]:
    """
    Zooms in on an array by repeating each element a given number of times.

    Args:
        lst (List[int]): The input list of integers.
        factor (int, optional): The factor by which to zoom in. Defaults to 2.

    Returns:
        Tuple[int]: The zoomed-in array as a tuple.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)


if __name__ == "__main__":
    array = [12, 72, 91]

    zoom_2x = zoom_array(array)

    zoom_3x = zoom_array(array, 3)

    print(zoom_2x)
    print(zoom_3x)
