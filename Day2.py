"""
Prompt:
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#   4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/


from typing import Any


# Given:
class Node:
    """
    A node in a binary tree (given to us).
    Has a value, and the nodes on the left and right below it.
    """

    def __init__(self, val: Any, left: Any = None, right: Any = None):
        """
        Creates a new node with the given value and leaves.
        :param val: value of this node
        :param left: the Node or value to the left of this Node
        :param right: the Node or value to the right of this Node
        """
        self.val: Any = val
        self.left: Any = left
        self.right: Any = right


def serialize(node: Node) -> str:
    """
    This turns a `Node` into a string. This basically just returns the repr of the `Node` according to the Python
    recommended style guide.
    :param node: `Node` to be serialized
    :return: str representation of the `Node`
    """
    return "Node(" + \
           repr(node.val) + \
           ", " + \
           str((isinstance(node.left, Node) and serialize(node.left)) or repr(node.left)) + \
           ", " + \
           str((isinstance(node.right, Node) and serialize(node.right)) or repr(node.right)) + \
           ")"


# They didn't say that the code had to be safe!
def deserialize(node: str) -> Node:
    """
    The input string representation of the `Node` should be `eval`able. This is very unsafe and proper parsing is the
    best. There are issues with the fact that the problem did not specify that the val had to be a string so this was a
    decent trade off. A better way to do this would be to use Pickles for the non-Node objects.
    :param node: String representation of the `Node`.
    :return: deserialized `Node`
    """
    return eval(node)


test_node = Node('root', Node('left', Node('left.left')), Node('right'))
print(deserialize(serialize(test_node)).left.left.val == 'left.left')
