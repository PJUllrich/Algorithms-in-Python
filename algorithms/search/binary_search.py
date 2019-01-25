from math import floor
from typing import Optional


def binary_search(arr: [], val: int) -> Optional[int]:
    """
    Implementation of the Binary Search algorithm. Searches for value in a
    sorted list.

    :param arr: The list in which the algorithm searches.
    :param val: The value that is searched for.
    :return: Returns the index of the value in the list or None if not found.
    """
    low: int = 0
    high: int = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < val:
            low = mid + 1
        elif arr[mid] > val:
            high = mid - 1
        else:
            return mid

    return None
