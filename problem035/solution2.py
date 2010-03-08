"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
if __name__ == "__main__":
    import sys, os
    sys.path.append( os.path.join( os.getcwd(), '..' ) )

from datetime import datetime
from copy import copy
from threading import Thread

from euler_tools.prime import is_prime
from euler_tools.progress_bar import ProgressBar
from euler_tools.misc import is_palindrome

class PrimeGeneratorManager():
    def __init__(self):
        self.primes = []
        self.current = 2
        self.my_threads = []

    def next(self):
        if not self.current:
            self.current = 2
        else:
            tmp = self.current + 1
            while not is_prime(tmp, self.primes):
                tmp += 1

        self.primes.append = [self.current]
        return self.current

    def agent_finished(self, agent):
        self.primes.extend(agent.retval)
        self.start_agent()

    def start_agent(self):
        print "Starting agent"
        t = PrimeGeneratorAgent(self.current, self.current + 100000, self)
        t.start()
        self.my_threads.append(t)




class PrimeGeneratorAgent(Thread):
    def __init__(self, min_value, max_value, manager):
        Thread.__init__(self)
        self.primes = copy(manager.primes)
        self.min_value = min_value
        self.max_value = max_value

    def run(self):
        self.retval = []
        for n in range(self.min_value, self.max_value + 1):
            if is_prime(n):
                #~ print "Found prime: %s" % n
                self.retval.append(n)


        #~ self.primes.append = [self.current]
        #~ return self.current




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

#~ find_solution()

m = PrimeGeneratorManager()
#~ my_threads = []
for n in range(3):
    m.start_agent()
    #~ t = PrimeGeneratorAgent(1000000 * n, 1000000 * (n + 1), m)
    #~ t.start()
    #~ my_threads.append(t)

#~ for item in m.my_threads:
for item in m:
    print "Wait..."
    item.join()

#~ answer: 55
#~ 0:00:26.071487
