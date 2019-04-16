"""
Prompt:
Given the root to a binary tree, count the total number of nodes there are
"""
__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#  4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/


from util.tree import Node


def count_nodes(tree: Node) -> int:
    """
    Counts the number of nodes on a binary tree.
    :param tree: the binary tree to count the nodes of
    :return: the number of nodes in that tree
    """
    count = 1
    if tree.left is not None:
        count += count_nodes(tree.left)
    if tree.right is not None:
        count += count_nodes(tree.right)
    return count


if __name__ == "__main__":
    test = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    print(count_nodes(test))
