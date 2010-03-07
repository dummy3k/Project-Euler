"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6^(th) prime is 13.

What is the 10001^(st) prime number?
"""
if __name__ == "__main__":
    import sys, os
    sys.path.append( os.path.join( os.getcwd(), '..' ) )

from euler_tools.prime import is_prime

n = 2
for counter in range(10001):
    while not is_prime(n):
        n += 1

    print "#%s\t%s" % (counter, n)
    n += 1
