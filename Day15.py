"""
Prompt:
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish
this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""
__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#  4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/


log: list = []
N: int = 10


def record(order_id: int) -> None:
    """
    Add a record to the log.
    :param order_id: the order id to add
    :return: None
    """
    if len(log) < N:
        log.append(order_id)
    else:
        log.pop(0)
        log.append(order_id)


def get_last(i: int) -> int:
    """
    get the ith last element from the log.
    :param i: how many elements from the end (starts at 1)
    :return: the element
    """""
    return log[-i]


if __name__ == "__main__":
    for j in range(33):
        record(j)
    for j in range(N):
        print(get_last(j + 1), end=" ")
    print()
