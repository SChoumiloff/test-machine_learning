#!/usr/bin/env python3
"""
Module to concatenate arrays.
"""


def cat_arrays(arr1: list, arr2: list) -> list:
    """
    Concatenates two arrays.

    Args:
        arr1 (list): The first array.
        arr2 (list): The second array.

    Returns:
        list: A new list containing elements from both arrays.
    """
    def add_list(lst: list, arr: list) -> list:
        """
        Adds elements of an array to a list.

        Args:
            lst (list): The list to add elements to.
            arr (list): The array whose elements are added.

        Returns:
            list: The updated list.
        """
        for i in range(len(arr)):
            lst.append(arr[i])
        return lst

    liste = []
    add_list(liste, arr1)
    add_list(liste, arr2)
    return liste
