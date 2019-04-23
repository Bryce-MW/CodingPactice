"""
Prompt:
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each
subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results.
You can simply print them out as you compute them.
"""
__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#  4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/


def maxes(input_array, k):
    first_k = input_array[:k]
    input_array = input_array[k:]
    maximum = max(first_k)
    print(maximum)
    for number in input_array:
        temp = first_k.pop(0)
        if temp == maximum:
            maximum = max(first_k)
        if number > maximum:
            maximum = number
        first_k.append(number)
        print(maximum)


if __name__ == "__main__":
    maxes([10, 5, 2, 7, 8, 7], 3)
