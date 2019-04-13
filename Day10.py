"""
Prompt:
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all
trings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""
__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#   4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/


from typing import Union, List


class Element:
    """
    An element of a tree.
    """
    def __init__(self, value):
        """
        Creates a new `Element` and sets the value to the value.
        :param value: the value of the element
        """
        self.below: list = []
        self.value: str = value


def add_string(element: Element, option: str) -> None:
    """
    Adds a string to the tree.
    :param element: the base of the tree
    :param option: the string to add
    :return: None
    """
    current_element = element
    for letter in option:
        element_present = False
        for sub_element in current_element.below:
            if sub_element.value == letter:
                element_present = sub_element
        if element_present:
            current_element = element_present
        else:
            new_element = Element(letter)
            current_element.below.append(new_element)
            current_element = new_element
    current_element.below.append(Element(""))


def traverse(element: Element, option: str) -> Union[Element, None]:
    """
    Traverses the tree to the point of the end of the string.
    :param element: the base of the tree
    :param option: the string to traverse
    :return: None
    """
    current_element: Element = element
    for letter in option:
        element_present = False
        for sub_element in current_element.below:
            if sub_element.value == letter:
                element_present = sub_element
        if element_present:
            # The following inspection is disabled because if element_present is not False, then it is an Element
            # noinspection PyTypeChecker
            current_element = element_present
        else:
            return None
    return current_element


def show_tree(element: Element) -> List[str]:
    """
    Show all strings in the tree.
    :param element: the base of the tree
    :return: the list of strings in the tree
    """
    strings: List[str] = []
    for option in element.below:
        if option.value == "":
            strings.append(element.value)
        else:
            for string in show_tree(option):
                strings.append(element.value + string)
    return strings


def auto_complete(element: Element, option: str) -> List[str]:
    """
    Returns the possible values based on a starting value.
    :param element: the base of the auto-complete tree
    :param option: the string to search for
    :return: the list of possible strings
    """
    return [option[:-1] + j for j in show_tree(traverse(element, option))]


if __name__ == "__main__":
    translator = Element("")
    for i in ["dog", "deer", "deal"]:
        add_string(translator, i)
    print(auto_complete(translator, "de"))
