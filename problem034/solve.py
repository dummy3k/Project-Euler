import math
from euler_tools.misc import StopWatch, LossyPrinter

#~ N: 102239423
lp = LossyPrinter(1)

try:
    for n in range(3, math.factorial(9)):
    #~ n = 145
    #~ n = 2
    #~ while True:
        n += 1
        lp.try_print(n)
        sum = 0
        for digit in str(n):
            digit = int(digit)
            #~ print digit, math.factorial(digit)
            sum += math.factorial(digit)
            if sum > n:
                break

        if sum == n:
            print "Found one: %s" % n
        #~ if sum > n:
            #~ print "No"
    #~ print "Sum: %s" % sum
except KeyboardInterrupt:
    print "\nN: %s" % n
