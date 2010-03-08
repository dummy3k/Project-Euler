"""
The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from
left to right and right to left.
"""
if __name__ == "__main__":
    import sys, os
    sys.path.append( os.path.join( os.getcwd(), '..' ) )

from euler_tools.prime import is_prime

def is_truncatable(number):
    if not is_prime(number):
        return False

    number_str = str(number)
    for n in range(1, len(number_str)):
        truncated = int(number_str[:-n])
        if not is_prime(truncated):
            #~ print truncated
            return False

        truncated = int(number_str[n:])
        #~ print truncated
        if not is_prime(truncated):
            return False
    # from left to right

    return True

def do_it_old(number, depth):
    print "enter do_it: %s" % number
    for n in range(10):
        sub_number = int(str(n + 1) + str(number))
        if is_truncatable(sub_number):
            print str(sub_number) + "*"
            if depth < 10:
                do_it(sub_number, depth + 1)
        #~ else:
            #~ print sub_number

        sub_number = int(str(number) + str(n + 1))
        if is_truncatable(sub_number):
            print str(sub_number) + "*"
            if depth < 10:
                do_it(sub_number, depth + 1)
        else:
            print sub_number




#~ do_it(7, 0)

solutions = []

def do_it(number, depth):
    solution_count = 0
    #~ print "do_it(%s, %s)" % (number, depth)
    for append_this in range(10):
        #~ check_this = int(str(number) + str(append_this))
        check_this = number * 10 + append_this
        if is_prime(check_this):
            #~ print check_this
            do_it(int(check_this), depth + 1)

            if is_truncatable(check_this):
                solutions.append(check_this)
                #~ print "Solution: %s" % check_this
                #~ solution_count += 1


    #~ return solution_count

#~ do_it([2, 3, 5, 7], 0)
do_it(0, 0)

def filter(sequence, fn):
    retval = []
    for item in sequence:
        if fn(item):
            retval.append(item)

    return retval

solutions.sort()
solutions = filter(solutions, lambda x: x > 10)
print "solutions: %s" % solutions
print "solutions count: %s" % len(solutions)
print "solutions sum: %s" % reduce(lambda r, x: r + x, solutions)

#~ print "solution_count: %s" % do_it(0, 0)

#~ print is_truncatable(379)
