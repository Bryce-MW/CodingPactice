"""
Prompt:
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If
there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return
null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return
['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either
['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""
from collections import defaultdict

__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#  4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/

from typing import List


def originate(combined: str, dictionary: List[str]) -> List[str]:
    """
    Finds the list of the original sentence for one with the removed spaces
    :param combined:
    :param dictionary:
    :return:
    """
    if combined == "":
        return [" "]
    starters: List[str] = [i for i in dictionary if combined.startswith(i)]
    if not starters:
        return []
    options: List[List[str]] = [[i] + j for i in starters if (j:= originate(combined[len(i):], dictionary))]
    if not options:
        return []
    return [i for i in options[0] if i.rstrip()]


if __name__ == "__main__":
    print(f"{originate('thequickbrownfox', ['quick', 'brown', 'the', 'fox']) = }")
    print(f"{originate('bedbathandbeyond', ['bed', 'bath', 'bedbath', 'and', 'beyond']) = }")
