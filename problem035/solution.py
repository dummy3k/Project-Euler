"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
if __name__ == "__main__":
    import sys, os
    sys.path.append( os.path.join( os.getcwd(), '..' ) )

from datetime import datetime
from copy import copy

from euler_tools.prime import is_prime
from euler_tools.progress_bar import ProgressBar
from euler_tools.misc import is_palindrome

def permutate(sequence, result, fn):
    #~ print "permutate(%s, %s)" % (sequence, seq_str)

    if len(sequence) == 0:
        #~ return [seq_str]
        fn(result)

    #~ retval = []
    for item in sequence:
        sub_sequence = copy(sequence)
        sub_sequence.remove(item)
        sub_result = copy(result)
        sub_result.append(item)
        permutate(sub_sequence, sub_result, fn)
        #~ retval.extend(permutate(sub_sequence, seq_str + item))


    #~ return retval

class IsNotPrimeError(Exception):
    pass

def raise_if_not_prime(char_array):
    tmp_str = reduce(lambda r, x: r + str(x), char_array, "")
    if not is_prime(int(tmp_str)):
        raise IsNotPrimeError("is not prime: " + tmp_str)


def find_solution():
    start_time = datetime.now()
    answer = 0
    primes = []
    progress = ProgressBar(1000000)

    for n in xrange(2, progress.max):
        progress.set_value(n)

        if is_prime(n, primes):
            primes.append(n)

            #~ digits = map(lambda x: int(x), str(n))
            try:
                permutate(map(lambda x: x, str(n)), [], raise_if_not_prime)
                print "Found palindrome: %s" % n
                answer += 1

            except IsNotPrimeError:
                pass

            #~ all_prime = True
            #~ for item in permutate(map(lambda x: x, str(n)), ""):
                #~ if not is_prime(int(item)):
                    #~ all_prime = False
                    #~ break

            #~ if all_prime:

    end_time = datetime.now()
    progress.finished()
    print "answer: %s" % answer
    print "number of primes: %s" % len(primes)
    print "first 10 primes: %s" % primes[:10]
    print end_time - start_time

n = 197
def print_x(x):
    print x
#~
digits = map(lambda x: int(x), str(n))
#~ print permutate(digits, [], lambda x: x)
#~ find_solution()

permutate(digits, [], raise_if_not_prime)
#~ try:
    #~ permutate(digits, [], raise_if_not_prime)
    #~ print "Is Prime!"
#~ except IsNotPrimeError:
    #~ print "Is NO Prime!"





#~ answer: 22
#~ 0:07:00.911644

