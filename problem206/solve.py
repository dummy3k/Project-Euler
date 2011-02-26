#~ Find the unique positive integer whose square has the
#~ form 1_2_3_4_5_6_7_8_9_0, where each "_" is a single digit.
import re, math
from euler_tools.misc import LossyPrinter
lp = LossyPrinter(2)

def slow():
    #~ Solution found:
    #~ 1929374254627488900
    #~ 1389019170

    #                     1_2_3_4_5_6_7_8_9_0
    min_n = int(math.sqrt(1020304050607080900))
    max_n = int(math.sqrt(1929394959697989990))
    print "%s/%s" % (min_n, max_n)
    max_n += (10 - max_n % 10)
    print "%s/%s" % (min_n, max_n)


    myre = re.compile('1.2.3.4.5.6.7.8.9.0')
    #~ for n in xrange(min_n, max_n, 10):
    for n in xrange(max_n, min_n, -10):
        s = n * n
        lp.try_print("n: %s, s: %s" % (n, s))
        if myre.match(str(s)):
            print "Solution found:"
            print s
            print n
            break


def slower():
    for n1 in range(10):
        for n2 in range(10):
            for n3 in range(10):
                for n4 in range(10):
                    for n5 in range(10):
                        for n6 in range(10):
                            for n7 in range(10):
                                for n8 in range(10):
                                    for n9 in range(10):
                                        #~ n = "1%s2%s3%s4%s5%s6%s7%s8%s9%s0" % (n1, n2, n3, n4, n5, n6, n7, n8, n9)
                                        #~ lp.try_print(n)
                                        lp.try_print("doo")


slow()
