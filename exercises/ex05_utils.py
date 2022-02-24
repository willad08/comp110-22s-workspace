"""Utilizing lists and then corresponding tests."""

__author__ = "730229417"


def only_evens(evens: list[int]) -> list[int]:
    """Returning only even numbers in a list."""
    i: int = 0
    output: list[int] = list()
    while i < len(evens):
        if evens[i] % 2 != 0:
            output.pop((evens[i]))
        i += 1
    return output


def sub(list1: list[int], begin: int, finish: int) -> list[int]:
    """Returns subset of a list."""
    if len(list1) == 0:
        return []
    if begin >= len(list1):
        return []
    if finish <= 0:
        return []
    if begin < 0:
        return [list1[0], list1[finish - 1]]
    if finish > len(list1):
        return [list1[begin], list1[len(list1) - 1]]
    else:
        return [list1[begin], list1[finish - 1]]


def concat(list_a: list[int], list_b: list[int]) -> list[int]:
    """Summing two lists to make one large list."""
    i: int = 0
    template: list[int] = list_a
    while i < len(list_b):
        template.append(list_b[i])
        i += 1
    return template
