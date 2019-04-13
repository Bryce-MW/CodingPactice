"""
Prompt:
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

The `multi_pass` function uses my original method and the `single_pass` function uses only a single pass as is the bonus

When running in interactive mode, the first line of input determines if tests are run (if empty), or which pass mode
should be enabled.
"""
__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#   4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/


from typing import Sequence, Union, MutableSet, TypeVar
import itertools

Number = TypeVar('Number', int, float, complex)


def multi_pass(list_of_numbers: Sequence[Number], k: Union[int, float]) -> bool:
    """
    This version requires multiple passes of looking at the list.
    These passes are done in `itertools.combinations` but I still feel that it counts are multiple passes.
    This method, acceptable as is is much faster in terms of complexity.
    This method, like the other does add some time as it may search farther than required.
    This could be reduced if I did not like one liners so much.
    :param list_of_numbers: the list of numbers given
    :param k: the given k
    :return: a boolean representing if k can be constructed by adding two values in `list_of_numbers`
    """
    return any([True for pair in itertools.combinations(list_of_numbers, 2) if sum(pair) == k])


# Note that disabling the following inspection is ok because the set is cleared at the end since elements in Tuple
# literals are evaluated in the order specified
# noinspection PyDefaultArgument
def single_pass(list_of_numbers: Sequence[Number], k: Union[int, float], looking_for: MutableSet[Number] = set()) \
        -> bool:
    """
    This version requires only a single pass of the list however it will have to do multiple passes of the set.
    This is acceptable as is is much faster in terms of complexity.
    This method, like the other does add some time as it may search farther than required.
    This could be reduced if I did not like one liners so much.
    :param list_of_numbers: the list of numbers given
    :param k: the given k
    :param looking_for: a set used as a temporary variable, should never be provided
    :return: a boolean representing if k can be constructed by adding two values in `list_of_numbers`
    """
    return (any([True for number in list_of_numbers if number in looking_for or looking_for.add(k - number)]),
            looking_for.clear())[0]


if __name__ == "__main__":
    do_test: str = input()
    if not do_test:
        tests = \
            (([10, 15, 3, 7], 17, True),
             ([10, 15, 3, 7], 18, False))
        single_tests = [test[2] == single_pass(test[0], test[1]) for test in tests]
        print("single_pass passes all tests") if all([test is tests[i][2] for i, test in enumerate(single_tests)]) \
            else [print("Test " + str(tests[i]) + " failed for single_pass with " + str(test))
                  for i, test in enumerate(single_tests) if test is not tests[i][2]]
        multi_tests = [test[2] == multi_pass(test[0], test[1]) for test in tests]
        print("multi_pass passes all tests") if all([test is tests[i][2] for i, test in enumerate(multi_tests)]) else \
            [print("Test " + str(tests[i]) + " failed for multi_pass with " + str(test))
             for i, test in enumerate(multi_tests) if test is not tests[i][2]]

    elif do_test == "single":
        print(single_pass([int(i) for i in input().split()], int(input())))
    else:
        print(multi_pass([int(i) for i in input().split()], int(input())))
