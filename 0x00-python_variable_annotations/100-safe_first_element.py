#!/usr/bin/env python3

from typing import Sequence, Union


def safe_first_element(lst: Sequence) -> Union[object, None]:
    """
    Safely returns the first element of a sequence.

    Args:
        lst (Sequence): The input sequence.

    Returns:
        Union[object, None]: The first element of
        the sequence if it exists, else None.
    """
    if lst:
        return lst[0]
    else:
        return None


if __name__ == "__main__":
    print(safe_first_element.__annotations__)
