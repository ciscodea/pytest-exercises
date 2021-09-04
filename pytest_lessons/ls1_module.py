"""A lesson 1 example module."""

from typing import List

def total(xs: List[float]) -> float:
    """Total returns the sum of xs"""
    result: float = 0.0
    for x in xs:
        result += x

    return result

def join(xs: List[int], delimiter: str) ->str:
    """Produce a string where subsequent items are separated by delimiter."""
    generated_string: str = ""
    for item in xs:
        if generated_string == "":
            generated_string = str(item)
        else:
            generated_string += delimiter + str(item)

    return generated_string
