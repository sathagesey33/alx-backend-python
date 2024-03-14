#!/usr/bin/env python3
"""
Module for safely getting a value from a dictionary.
"""

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key:
                     Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely gets a value from a dictionary.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to retrieve the value for.
        default (Union[T, None], optional): The default value to return
        if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key, or the default
        value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default


if __name__ == "__main__":
    annotations = safely_get_value.__annotations__
    print("Here's what the mappings should look like")
    for k, v in annotations.items():
        print("{}: {}".format(k, v))
