"""
Prompt:
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example,
car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
"""
__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#   4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/


from typing import Callable, Any


# Given:
def cons(a: Any, b: Any) -> Callable[[Callable[[Any, Any], Any]], Any]:
    """
    Returns a pair of values.
    :param a: the first value in the pair
    :param b: the second value in the pair
    :return: the pair
    """
    def pair(f: Callable[[Any, Any], Any]):
        """
        Calls f on the objects on the pairs.
        :param f: function to call
        :return: the output of the function
        """
        return f(a, b)
    return pair


def car(pair: Callable[[Callable[[Any, Any], Any]], Any]) -> Any:
    """
    Returns the first value in a pair.
    :param pair: the pair
    :return: the first value in the pair
    """
    return pair(lambda a, b: a)


def cdr(pair: Callable[[Callable[[Any, Any], Any]], Any]) -> Any:
    """
    Returns the second value in a pair.
    :param pair: the pair
    :return: the second value in the pair
    """
    return pair(lambda a, b: b)


if __name__ == "__main__":
    print(str(car(cons(3, 4))))
    print(str(cdr(cons(3, 4))))
