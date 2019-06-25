"""
Prompt:
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""
__author__ = "Bryce Wilson"


#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#  4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/

class Element:
    """
    An element of a single linked list. Has one reference to the next element
    """

    def __init__(self, next_element):
        self.next_element: Element = next_element


def find_overlap(list1: Element, list2: Element) -> Element:
    """
    Finds the element where both lists become one
    :param list1: the first list
    :param list2: the second list
    :return: the element where the lists combine
    """
    special_element = Element(None)

    current_element = list2
    while current_element.next_element is not None:
        next_element = current_element.next_element
        current_element.next_element = special_element
        current_element = next_element

    current_element = list1
    while current_element.next_element is not special_element:
        current_element = current_element.next_element
    return current_element


if __name__ == "__main__":
    first = Element(None)
    second = first

    for i in range(5):
        first = Element(first)
        if i == 3:
            second = first

    for i in range(5):
        second = Element(first)

    print(f"{find_overlap(first, second) = }")
