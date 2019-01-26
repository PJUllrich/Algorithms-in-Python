import random


def quick_sort(arr: list, start: int = None, end: int = None):
    """
    Implementation of the Quick Sort algorithm. Sorts a list with time
    complexity of O(n log n) and space complexity of O(log n).

    :param arr: The list to be sorted
    :param start: The start index of from where the list should be sorted
    :param end: The end index until which the list should be sorted.
    """
    start = 0 if start is None else start
    end = len(arr) - 1 if end is None else end

    if start < end:
        piv_idx = random.randint(start, end)
        arr[piv_idx], arr[start] = arr[start], arr[piv_idx]

        piv = arr[start]
        pos = start
        for j in range(start + 1, end + 1):
            if arr[j] < piv:
                pos += 1
                arr[j], arr[pos] = arr[pos], arr[j]

        arr[start], arr[pos] = arr[pos], arr[start]

        quick_sort(arr, start, pos - 1)
        quick_sort(arr, pos + 1, end)
