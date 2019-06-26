"""
Prompt:
You have an N by N board. Write a function that returns the number of possible arrangements of the board where N queens
can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.
"""
from typing import List

__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#  4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/


def place(test_board: List[List[bool]], pos: int, row: int) -> List[List[bool]]:
    """
    Returns a new board with the queen placed
    :param test_board: The staring board
    :param pos: The column of the queen
    :param row: The row of the queen
    :return:
    """
    return [[bool(
        i == pos or
        j == row or
        i - pos == j - row or
        pos - i == j - row)
        for j in range(len(test_board[0]))] for i in range(len(test_board))]


def check_pos(test_board: List[List[bool]], pos: int, row: int) -> int:
    """
    Counts the number of possible positions if a queen is in the specified location
    :param test_board: The current board
    :param pos: The tentative column
    :param row: The tentative row
    :return: The number of possible positions
    """
    new_board = test_board.copy() if test_board[pos][row] else place(test_board, pos, row)
    if row + 1 != len(test_board[0]):
        count = 0
        for i in range(len(test_board)):
            count += check_pos(new_board, i, row + 1)
        return count
    else:
        return 1


def queens(k: int, n: int) -> int:
    """
    Returns the number of ways that queens can be placed on a k×n board without threatening each other
    :param k: One dimension
    :param n: The other dimension
    """
    test_board = [[False] * n for ignored in range(k)]
    count = 0
    for i in range(k):
        count += check_pos(test_board, i, 0)
    return count


if __name__ == "__main__":
    print(f"{queens(1, 1) = }")
    print(f"{queens(2, 2) = }")
    print(f"{queens(3, 3) = }")
    print(f"{queens(4, 4) = }")
