#!/usr/bin/env python3

def add_arrays(arr1, arr2):
    """
    Add two arrays element-wise.

    Args:
        arr1 (list): First array.
        arr2 (list): Second array.

    Returns:
        list: A new array with the element-wise sum of arr1 and arr2.

    Raises:
        SystemExit: If the arrays are not of the same length.
    """
    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr2))]
