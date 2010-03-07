"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
if __name__ == "__main__":
    import sys, os
    sys.path.append( os.path.join( os.getcwd(), '..' ) )

from datetime import datetime

from euler_tools.prime import is_prime
from euler_tools.progress_bar import ProgressBar

start_time = datetime.now()
sum = 0
primes = []
progress = ProgressBar(2000000)

for n in xrange(2, progress.max):
    progress.set_value(n)

    if is_prime(n, primes):
        sum += n
        primes.append(n)

end_time = datetime.now()
progress.finished()
print "sum: %s" % sum
print "number of primes: %s" % len(primes)
print end_time - start_time

#2,000,000: 142913828922

