import math

def is_prime(number, primes=None):
    start_at = 2

    #~ if reduce(lambda x, y: x or (number % y == 0), primes, False):
        #~ return False

    #~ for m in primes:
        #~ foobar = m

    square_root = int(math.sqrt(number))
    if not primes:
        start_at = 2
    else:
        for m in primes:
            if m > square_root:
                break

            if number % m == 0:
                return False

        start_at = m + 1


    for divisor in xrange(start_at, square_root + 1):
        if number % divisor == 0:
            return False

    return True
