"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
if __name__ == "__main__":
    import sys, os
    sys.path.append( os.path.join( os.getcwd(), '..' ) )

import sys
from datetime import datetime
from euler_tools.prime import is_prime

class ProgressBar():
    def __init__(self, max):
        self.max = max
        self.value = 0
        self.last_update = None
        self.tty_width = 40

    def set_value(self, value):
        if value == self.value:
            return

        self.value == value
        if not self.last_update or (datetime.now() - self.last_update).seconds > 1:
            percent = value * 1. / self.max
            msg = "\r["
            for n in range(self.tty_width - 2):
                if float(n) / self.tty_width > percent:
                    msg += "_"
                else:
                    msg += "*"

            #~ print "\r%s" % percent,
            msg += "]"
            print msg,
            sys.stdout.flush()
            self.last_update = datetime.now()

    def finished(self):
        msg = "\rFinished"
        while len(msg) - 1 < self.tty_width:
            msg += " "

        print msg

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

