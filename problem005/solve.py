#~ 2520 is the smallest number that can be divided by each of the
#~ numbers from 1 to 10 without any remainder.
#~
#~ What is the smallest positive number that is evenly divisible by all
#~ of the numbers from 1 to 20?
from euler_tools.misc import LossyPrinter

def solve2():
    t = timeit.Timer("solve2()")
    t.timeit()
    t.print_exc()


def solve():
    lp = LossyPrinter(1)
    problem_space = 20
    #~ start = timeit.time.time()
    #~ divisors = [2, 3, 5, 7, 9, 11, 13, 17, 19]
    #~ divisors = [2, 3, 5, 7, 9, 11, 13, 17]
    # 20, 19, 18, 17, 16, 15, 14, 13, 12, 11
    divisors = range(problem_space, problem_space / 2, -1)
    #~ divisors = range(2, problem_space + 1)
    #~ divisors.reverse()
    for n in xrange(problem_space, 1000000000, problem_space):
        lp.try_print("Testing: %s" % n)
        success = True
        for m in divisors:
            #~ print "%s %% %s = %s" % (n, m, n % m)
            if n % m != 0:
                success = False
                break

        if success:
            print "SUCCESS: %s" % n
            break

