import doctest
import math
from euler_tools.misc import StopWatch

max_perimeter = 1001

def cnt_solutions(perimeter):
    """
        >>> cnt_solutions(120)
        3
    """
    retval = 0
    for a in range(1, perimeter / 2):
        for b in range(a + 1, perimeter / 2):
            c = perimeter - a -b
            if a ** 2 + b ** 2 == c ** 2:
                #~ print "%s^2 * %s^2 = %s^2" % (a, b, c)
                retval += 1

            #for c in range(b + 1, perimeter):
                #if a ** 2 + b ** 2 == c ** 2 and a + b + c == perimeter:
                    ##~ print "%s^2 * %s^2 = %s^2" % (a, b, c)
                    #retval += 1

    return retval

def main():
    watch = StopWatch()
    
    max_length = 0
    for d in range(1, 1001):
        length = cnt_solutions(d)
        if length > max_length:
            print "%s -> %s" % (d, length)
            max_length = length

    watch.print_time()

    # 840 -> 8
    
if __name__ == '__main__':
    doctest.testmod()
    main()
