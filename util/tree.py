"""
Implementation of a binary tree based on the implementation given on Day2
"""
__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#   4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/


from typing import Any


class Node:
    """
    A node in a binary tree (given to us).
    Has a value, and the nodes on the left and right below it.
    """
    def __init__(self, val: Any, left=None, right=None):
        """
        Creates a new node object with the specified value and optional left and right nodes.
        :param val: the value of this node
        :param left: the node to the left
        :param right: the node to the right
        """
        self.val: Any = val
        self.left: Node = left
        self.right: Node = right
