"""
Prompt:
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x^2 + y^2 = r^2.

The Monte Carlo method works by finding the ratio between points inside and outside the circle.
This one does not make much sense as a function so I will make it a script with no __name__ == "__main__" protection.
"""
__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#  4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/


import random

SAMPLES: int = 2000000  # this appears to be large enough to almost always get 3.14 as the first three digits
outside: int = 0
inside: int = 0

for i in range(SAMPLES):
    if random.uniform(-1, 1) ** 2 + random.uniform(-1, 1) ** 2 <= 1:
        inside += 1
    else:
        outside += 1

# inside / (inside + outside) = π / 4
# π = 4*inside / (inside + outside)

pi_approx = 4 * inside / (outside + inside)

if __name__ == "__main__":
    print(str(pi_approx)[:4])
