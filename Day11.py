"""
Prompt:
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function
that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive
integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""
__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#   4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/


from typing import List


def two_steps(number_of_steps: int) -> int:
    if number_of_steps == 1:
        return 1
    elif number_of_steps == 2:
        return 2
    else:
        return two_steps(number_of_steps-1) + two_steps(number_of_steps-2)


def n_steps(number_of_steps: int, options: List[int]) -> int:
    if number_of_steps == 0:
        return 1
    count: int = 0
    for option in options:
        if number_of_steps >= option:
            count += n_steps(number_of_steps-option, options)
    return count


if __name__ == "__main__":
    print(two_steps(4))
    print(n_steps(4, [1, 2]))
    print(n_steps(10, [1, 3, 5]))
