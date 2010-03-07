import math

def is_prime(number, primes=None):
    if not primes:
        start_at = 2
    else:
        for m in primes:
            if number % m == 0:
                return False

        start_at = m + 1


    for divisor in range(start_at, int(math.sqrt(number)) + 1):
        if number % divisor == 0:
            return False

    return True
