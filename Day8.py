"""
Prompt:
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or
negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5
and 5.

Follow-up: Can you do this in O(N) time and constant space?

Note: I misread and thought it was just two non-adjacent numbers but I am too lazy at the moment to write a new proper
version. Perhaps another day.
"""
__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#   4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/


import itertools
from typing import List, Tuple, Union


def largest_sum(numbers: List[int]) -> int:
    """
    Returns the maximum sum of non-adjacent numbers. This has a large time and space complexity.
    :param numbers: list of numbers to analise
    :return: the maximum sum of non-adjacent numbers
    """
    pairs: List[Tuple[int]] = [tuple(numbers[i:i+2]) for i in range(len(numbers)-1)]
    complete_pairs: List[Tuple[int]] = list(itertools.combinations(numbers, 2))
    for pair in pairs:
        complete_pairs.remove(pair)
    maximum: int = complete_pairs[0][0] + complete_pairs[0][1]
    for pair in complete_pairs:
        if pair[0] + pair[1] > maximum:
            maximum = pair[0] + pair[1]
    return maximum


def constant_space(numbers: List[int]) -> int:
    """
    Returns the maximum sum of non-adjacent numbers. This is O(n) and constant space.
    :param numbers: list of numbers to analise
    :return: the maximum sum of non-adjacent numbers
    """
    maximum_total: Union[int, None] = None
    maximum: Union[int, None] = None
    current: Union[int, None] = None
    for number in numbers:
        if current is not None:
            if maximum is not None:
                if maximum_total is not None:
                    if number + maximum > maximum_total:
                        maximum_total = number + maximum
                else:
                    maximum_total = number + maximum
            else:
                maximum = current
            if current > maximum:
                maximum = current
        current = number
    return maximum_total


if __name__ == "__main__":
    print(largest_sum([2, 4, 6, 2, 5]))
    print(constant_space([2, 4, 6, 2, 5]))
    print(largest_sum([5, 1, 1, 5]))
    print(constant_space([5, 1, 1, 5]))
