import doctest
from euler_tools.misc import StopWatch, LossyPrinter
from euler_tools.prime import is_prime, gen_primes

primes = [2]
max_n = 28123
#~ max_n = 100

def is_abundant_prime(n):
    """
        #>>> is_abundant_prime(2)
        #False
        #>>> is_abundant_prime(6)
        #False
        #>>> is_abundant_prime(6)
        #False
        x>>> is_abundant_prime(12)
        True
    """
    #~ sum = 0
    #~ for m in xrange(1, n):
    sum = 1
    for m in gen_primes(n - 1, primes):
        if n % m == 0:
            print "m: %s" % m
            sum += m
            if sum > n:
                return True

    return (sum > n)

def is_abundant_naive(n):
    """
        >>> is_abundant_naive(0)
        False
        >>> is_abundant_naive(2)
        False
        >>> is_abundant_naive(6)
        False
        >>> is_abundant_naive(12)
        True
        >>> is_abundant_naive(83)
        False
        >>> is_abundant_naive(60)
        True
    """
    sum = 0
    for m in xrange(1, n / 2 + 1):
        if n % m == 0:
            sum += m
            if sum > n:
                return True

    return (sum > n)

def is_sum_of_abundant_numbers(n, abundant_numbers):
    """
        abundant numbers < 100
        >>> an = [12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88, 90, 96]
        >>> is_sum_of_abundant_numbers(30, an)
        True
        >>> is_sum_of_abundant_numbers(31, an)
        False
        >>> is_sum_of_abundant_numbers(84, an)
        True
        >>> is_sum_of_abundant_numbers(83, an)
        False
        >>> is_sum_of_abundant_numbers(85, an)
        False
    """
    for sumand_1 in abundant_numbers:
        if sumand_1 > n:
            return False

        if divide_conquer(n, sumand_1, abundant_numbers, 0, len(abundant_numbers), 0):
            return True

    return False

def divide_conquer(n, sumand_1, abundant_numbers, left, right, depth):
    di = " " * depth
    #~ print "%sdivide_conquer(%s, %s, %s, %s)" % (di, n, sumand_1, left, right)
    #~ if depth > 5:
        #~ print "max depth"
        #~ return

    if left >= right:
        #~ print "left >= right"
        return False


    pivot_index = left + (right - left) / 2
    try:
        #~ if pivot_index < 0 or pivot_index:
            #~ return False
        pivot_value = abundant_numbers[pivot_index]
    except IndexError:
        raise IndexError("idx: %s, len: %s, left: %s, right: %s" % (pivot_index, len(abundant_numbers), left, right))

    #~ print "  pivot_index: %s, pivot_value: %s " % (pivot_index, pivot_value)
    if sumand_1 + pivot_value == n:
        return True

    if right - left == 1:
        #~ print "%sbvlagh" % di
        return False

    if sumand_1 + pivot_value > n:
        #~ print "  go left"
        return divide_conquer(n, sumand_1, abundant_numbers, left, pivot_index, depth + 1)
    else:
        #~ print "  go right"
        return divide_conquer(n, sumand_1, abundant_numbers, pivot_index, right, depth + 1)

def main():
    lp = LossyPrinter(1)

    #~ max_n = 5000
    abundant_numbers = []
    for n in range(max_n):
        lp.try_print(n)
        if is_abundant_naive(n):
            abundant_numbers.append(n)

    #~ len(abundant_numbers): 6965

    print "len(abundant_numbers): %s"  % len(abundant_numbers)
    if len(abundant_numbers) < 100:
        print abundant_numbers

    sum = 0
    for n in range(max_n):
        lp.try_print("n: %s" % n)
        if not is_sum_of_abundant_numbers(n, abundant_numbers):
           sum += n

    #candidates = range(max_n)
    #for index, n in enumerate(abundant_numbers):
        #for m in abundant_numbers[index:]:
            #local_sum = n + m
            #if local_sum > max_n:
                #break

            #if local_sum in candidates:
                #lp.try_print("%s + %s = %s, removed, left: %s" % (n, m, local_sum, len(candidates)))
                #candidates.remove(local_sum)

    #print "len(candidates): %s" % len(candidates)
    #sum = reduce(lambda x, y: x + y, candidates)

    print "Anwser: %s" % sum
    # correct answer: 4179871
    if sum != 4179871:
        print "THIS IS INCORRECT!"



if __name__ == '__main__':
    an = [12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88, 90, 96]
    #~ print "foo: %s" % is_sum_of_abundant_numbers(30, an)


    failures, cnt_tests = doctest.testmod()
    if failures == 0:
        main()
        #~ for n in xrange(1, max_n):
            #~ if is_abundant(n) != is_abundant_naive(n):
                #~ print "is_abundant(%s): %s, is_abundant_naive(%s): %s" % (n, is_abundant(n), n, is_abundant_naive(n))
                #~ break

        ##~ foo = [x for x in gen_primes(28123, primes)]
        ##~ print len(foo)
        ##~ print foo[:10]
        ##~ pass
