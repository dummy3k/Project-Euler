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

def find_solution():
    start_time = datetime.now()
    answer = 0
    primes = []
    progress = ProgressBar(1000000)

    for n in xrange(2, progress.max):
        progress.set_value(n)

        if is_prime(n, primes):
            primes.append(n)

            all_prime = True
            for item in rotate(n):
                if not is_prime(int(item)):
                    all_prime = False
                    break

            if all_prime:
                print "Found palindrome: %s" % n
                answer += 1


    end_time = datetime.now()
    progress.finished()
    print "answer: %s" % answer
    print "number of primes: %s" % len(primes)
    print "first 10 primes: %s" % primes[:10]
    print end_time - start_time


def rotate(input):
    retval = []
    digits = map(lambda x: int(x), str(input))
    for index in range(len(digits)):
        tmp_seq = digits[index:]
        tmp_seq.extend(digits[0:index])
        #~ tmp_seq = input[0:index]
        tmp_str = reduce(lambda r, x: r + str(x), tmp_seq, "")
        retval.append(tmp_str)

    return retval

find_solution()

#~ n = 197
#~ print rotate(123456)


#~ def print_x(x):
    #~ print x
#~
#~ print permutate(digits, [], lambda x: x)

#~ permutate(digits, [], raise_if_not_prime)
#~ try:
    #~ permutate(digits, [], raise_if_not_prime)
    #~ print "Is Prime!"
#~ except IsNotPrimeError:
    #~ print "Is NO Prime!"





#~ answer: 22
#~ 0:07:00.911644

