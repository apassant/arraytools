# -*- coding: utf-8 -*-
"""
flatten.py - Flatten-related function of the arraytools module
"""

from config import array_types


def flatten(array_to_flatten, allowed_types=(object)):
    """
    Flatten arbitrarily nested "arrays" (see config.py) into a flat list, e.g.
    [[1, Foo() ,[3]], 'a'] -> [1, Foo(), 3, 'a']
    Note that empty list are skipped, e.g.
    [[1, Foo(), [3, []]], 'a'] -> [1, Foo(), 3, 'a']

    This iterates through each element of the array and:
    - recurse if it's an array, and add result to the initial array
    - append element if it's an allowed type
    - raise a TypeError exception otherwise

    Args:
        array_to_flatten ("array"): The array to flatten
        allowed_types (object_type, or tuple): The type(s) allowed in the array

    Returns:
        list: The flat array
    """
    if not isinstance(array_to_flatten, array_types):
        raise TypeError("Input must be in {array_types}".format(**{
            "array_types": array_types
        }))
    flat_array = []
    for element in array_to_flatten:
        if isinstance(element, array_types):
            flat_array += flatten(element)
        elif isinstance(element, allowed_types):
            flat_array.append(element)
        else:
            raise TypeError(
                "Array must contain {array_types} or {allowed_types}".format(**{  # noqa
                    "array_types": array_types,
                    "allowed_types": allowed_types
                }))
    return flat_array


def flatten_integers(array_to_flatten):
    """Extension of the flatten method, allowing for integers only."""
    return flatten(array_to_flatten, (int))
