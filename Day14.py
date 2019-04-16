"""
Prompt:
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""
__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#  4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/


import random
from typing import Any


# Let's assume that the stream is a list but we can only do a list.pop(0) and len(list) == 0 is when the end of the
# stream is reached
def equal_chance(stream: list) -> Any:
    """
    Produces an element from a stream with an equal chance of each
    :param stream: the stream (yes it's in list form but this is only an example)
    :return: one of the objects from the list
    """
    current_chance: int = 2
    current: Any = stream.pop(0)
    while len(stream) != 0:
        if not random.randrange(0, current_chance):
            current = stream.pop(0)
        else:
            stream.pop(0)
        current_chance += 1
    return current


if __name__ == "__main__":
    trials = 100000
    counts = [0, 0, 0, 0, 0]
    for i in range(trials):
        counts[equal_chance([0, 1, 2, 3, 4])] += 1
    print("Expected: " + str(trials // 5) + " each")
    print(counts)
    print("Average delta: " + str(sum([abs((trials // 5) - i) for i in counts]) // 5))
