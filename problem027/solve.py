import doctest
from euler_tools.prime import is_prime

def chain_length(a, b):
    """
        >>> chain_length(-79, 1601)
        80
        >>> chain_length(1, 41)
        40
    """
    n = 0
    while True:
        p = n ** 2 + a * n + b
        if not is_prime(p):
            break

        n += 1

    return n

max_length = 0
for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        length = chain_length(a, b)
        if length > max_length:
            print "%s, %s --> %s" % (a, b, length)
            max_length = length
            
if __name__ == '__main__':
    doctest.testmod()
