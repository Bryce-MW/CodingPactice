"""
Prompt:
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""
__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#   4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/


def longest_substring(input_string: str, letters: int) -> str:
    maximum: str = ""
    for i in range(len(input_string)):
        for j in range(len(input_string) - i):
            current = input_string[i:i + j]
            if len(current) > len(maximum) and len(set(current)) <= letters:
                maximum = current
    return maximum


if __name__ == "__main__":
    print(longest_substring("abcba", 2))
