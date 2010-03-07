"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6^(th) prime is 13.

What is the 10001^(st) prime number?
"""

import math

def is_prime(number):
    for divisor in range(2, int(math.sqrt(number)) + 1):
        if number % divisor == 0:
            return False

    return True


n = 2
for counter in range(10001):
    while not is_prime(n):
        n += 1

    print "#%s\t%s" % (counter, n)
    n += 1
