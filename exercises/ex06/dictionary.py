"""Fun with dictionaries (invert, count, and colors)."""

__author__ = "730229417"


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    """Inverting the values and keys of a dictionary."""
    dict_other: dict[str, str]
    dict_other = dict()
    for element in dict_1:
        dict_other[dict_1[element]] = element
    print(dict_other)
    return(dict_other)


def favorite_color(dict_2: dict[str, str]) -> str:
    """Returns the most popular color."""
    dict_other: dict[str, int]
    dict_other = dict()
    for name in dict_2:
        color = (dict_2[name])
        dict_other[color] = dict_other[color] + 1
    maxiumum: int
    color_1: str
    maximum = 0
    for color in dict_other:
        if maximum < dict_other[color]:
            maximum = dict_other[color]
            color_1 = color
    print(color_1)
    return color_1


def count(numbers: list[str]) -> dict[str, int]:
    """Counting the number of times a value appears in a list."""
    final: dict[str, int]
    final = dict()
    i = 0 
    len(numbers) <= 10
    while i < len(numbers):
        if i in final:
            i += 1
        else:
            i = 1
    return final