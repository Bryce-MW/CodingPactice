"""
Prompt:
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""
__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#   4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/


from typing import Any, List

from util.tree import Node


def is_unival_tree(tree: Node) -> bool:
    value: Any = tree.val
    nodes: List[Node] = [tree.left, tree.right]
    nodes = [node for node in nodes if node]
    while nodes:
        current: Node = nodes.pop(0)
        if current.val != value:
            return False
        if current.left:
            nodes.append(current.left)
        if current.right:
            nodes.append(current.right)
    return True


def number_of_is_unival_trees(tree: Node) -> int:
    """
    Returns the number of unival trees that are subtrees of the given tree.
    :param tree: the input tree
    :return: the number of unival trees
    """
    nodes: List[Node] = [tree.left, tree.right]
    nodes = [node for node in nodes if node]
    count: int = 0
    while nodes:
        current: Node = nodes.pop(0)
        if is_unival_tree(current):
            count += 1
        if current.left:
            nodes.append(current.left)
        if current.right:
            nodes.append(current.right)
    return count


if __name__ == "__main__":
    test = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    print(number_of_is_unival_trees(test))
