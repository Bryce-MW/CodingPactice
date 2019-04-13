"""
Prompt:

Given an array of integers, return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
[3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

`division` uses division and `non_division` does not.
"""
__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#   4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/


from typing import Iterable, List
import math


def division(multipliers: Iterable[int]) -> List[int]:
    """
    This method uses division and is relatively simple.
    :param multipliers: list of numbers to compute
    :return: list of computed numbers
    """
    return [math.prod(multipliers) // i for i in multipliers]


def non_division(multipliers: Iterable[int]) -> List[int]:
    """
    This method does not use division. It works by looping though the list but rather than just taking the product of
    the entire list, it filters out the current element.
    :param multipliers: list of numbers to compute
    :return: list of computed numbers
    """
    return [math.prod([new_selected for j, new_selected in enumerate(multipliers) if j != i])
            for i, selected in enumerate(multipliers)]


if __name__ == "__main__":
    do_test: str = input()
    if not do_test:
        tests = \
            (([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
             ([3, 2, 1], [2, 3, 6]))
        single_tests = [division(test[0]) for test in tests]
        print("single_pass passes all tests") if all([test == tests[i][1] for i, test in enumerate(single_tests)]) \
            else [print("Test " + str(tests[i]) + " failed for single_pass with " + str(test))
                  for i, test in enumerate(single_tests) if test is not tests[i][1]]
        multi_tests = [non_division(test[0]) for test in tests]
        print("multi_pass passes all tests") if all([test == tests[i][1] for i, test in enumerate(multi_tests)]) \
            else [print("Test " + str(tests[i]) + " failed for multi_pass with " + str(test))
                  for i, test in enumerate(multi_tests) if test is not tests[i][1]]
    elif do_test == "division":
        print(division([int(i) for i in input().split()]))
    else:
        print(non_division([int(i) for i in input().split()]))
