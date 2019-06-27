"""
Prompt:
You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each
False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the
end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right.
You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is
7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
"""
__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#  4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/

from typing import List, Tuple


def path(wall_map: List[List[bool]], pathed: List[List[bool]], loc: Tuple[int, int], final: Tuple[int, int]) -> int:
    if loc[0] + 1 == final[0] and loc[1] == final[1] or \
            loc[0] - 1 == final[0] and loc[1] == final[1] or \
            loc[1] + 1 == final[1] and loc[0] == final[0] or \
            loc[1] - 1 == final[1] and loc[0] == final[0] :
        return 1
    next_pathed = [[j for j in i] for i in pathed]
    try:
        next_pathed[loc[0] + 1][loc[1]] = True
    except IndexError:
        pass
    try:
        next_pathed[loc[0] - 1][loc[1]] = True
    except IndexError:
        pass
    try:
        next_pathed[loc[0]][loc[1] + 1] = True
    except IndexError:
        pass
    try:
        next_pathed[loc[0]][loc[1] - 1] = True
    except IndexError:
        pass
    options = []
    try:
        if not (wall_map[loc[0] + 1][loc[1]] or pathed[loc[0] + 1][loc[1]]):
            next_length = path(wall_map, next_pathed, (loc[0] + 1, loc[1]), final)
            if next_length:
                options.append(next_length + 1)
    except IndexError:
        pass
    try:
        if not (wall_map[loc[0] - 1][loc[1]] or pathed[loc[0] - 1][loc[1]]):
            next_length = path(wall_map, next_pathed, (loc[0] - 1, loc[1]), final)
            if next_length:
                options.append(next_length + 1)
    except IndexError:
        pass
    try:
        if not (wall_map[loc[0]][loc[1] + 1] or pathed[loc[0]][loc[1] + 1]):
            next_length = path(wall_map, next_pathed, (loc[0], loc[1] + 1), final)
            if next_length:
                options.append(next_length + 1)
    except IndexError:
        pass
    try:
        if not (wall_map[loc[0]][loc[1] - 1] or pathed[loc[0]][loc[1] - 1]):
            next_length = path(wall_map, next_pathed, (loc[0], loc[1] - 1), final)
            if next_length:
                options.append(next_length + 1)
    except IndexError:
        pass
    if not options:
        return 0
    return min(options)


if __name__ == "__main__":
    print(f"""{path([[False, False, False, False],
[True, True, False, True],
[False, False, False, False],
[False, False, False, False]],
[[False, False, False, False],
[False, False, False, False],
[False, False, False, False],
[False, False, False, False]], (3, 0), (0, 0)) = }""")
