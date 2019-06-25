"""
Prompt:
A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost
while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color,
return the minimum cost which achieves this goal.
"""
__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#  4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/

from typing import List


def minimise(cost_matrix: List[List[int]]) -> int:
    """
    Calculates the minimum cost to build the houses using the cost matrix `cost_matrix`
    :param cost_matrix: N by K matrix where the nth row and kth column represents the cost to build house n with color k
    :return: the minimum cost using this matrix
    """
    n: int = len(cost_matrix)
    k: int = len(cost_matrix[0])
    selections: List[int] = [0] * n
    min_cost = sum(j[i % 2] for i, j in enumerate(cost_matrix))
    while sum(selections) != (k - 1) * n:
        if all(i != j for i, j in zip(selections[1:], selections[:-1])):
            new_cost = sum(i[j] for i, j in zip(cost_matrix, selections))
            if new_cost < min_cost:
                min_cost = new_cost
        for i in range(len(selections)):
            if not i:
                selections[i] += 1
            else:
                if selections[i - 1] == k:
                    selections[i - 1] = 0
                    selections[i] += 1
    return min_cost


if __name__ == "__main__":
    example_matrix = [
        [1, 5, 7],
        [7, 4, 2],
        [6, 8, 1]
    ]
    print(f"""{minimise([
        [1, 5, 7],
        [7, 4, 2],
        [6, 8, 1]
    ]) = }""")
