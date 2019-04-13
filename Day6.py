"""
Prompt:
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""
__author__ = 'Bryce Wilson'
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#   4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/


from typing import List


def possibilities(input_string: str) -> int:
    """
    Returns how many possible ways they string can be decoded. Note that recursion is used.
    :param input_string: the string to check
    :return: the number of possibilities
    """
    if len(input_string) == 1:
        return 1
    elif len(input_string) == 2:
        if input_string[1] == "0":
            return 1
        else:
            if 10 <= int(input_string) <= 26:
                return 2
            else:
                return 1
    else:
        if input_string[1] == "0":
            return possibilities(input_string[2:])
        elif 10 <= int(input_string[:2]) <= 26:
            return possibilities(input_string[1:]) + possibilities(input_string[2:])
        else:
            return possibilities(input_string[1:])


def no_recursion(input_string: str) -> int:
    """
    Returns how many possible ways they string can be decoded. Note that recursion is not used.
    :param input_string: the string to check
    :return: the number of possibilities
    """
    count: int = 0
    stack: List[str] = [input_string]
    while stack:
        if len(stack[0]) == 1:
            count += 1
            stack.pop(0)
        elif len(stack[0]) == 2:
            if stack[0][1] == "0":
                count += 1
                stack.pop(0)
            else:
                if 10 <= int(stack[0]) <= 26:
                    count += 2
                    stack.pop(0)
                else:
                    count += 1
                    stack.pop(0)
        else:
            if stack[0][1] == "0":
                stack.append(stack[0][2:])
                stack.pop(0)
            elif 10 <= int(stack[0][:2]) <= 26:
                stack.append(stack[0][1:])
                stack.append(stack[0][2:])
                stack.pop(0)
            else:
                stack.append(stack[0][1:])
                stack.pop(0)
    return count


if __name__ == "__main__":
    print("Recursion:    111: " + str(possibilities("111")))
    print("No Recursion: 111: " + str(no_recursion("111")))
