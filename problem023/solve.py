import doctest
import multiprocessing
import math

from euler_tools.misc import StopWatch, LossyPrinter
from euler_tools.prime import is_prime, gen_primes

primes = [2]
max_n = 28123

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
    for m in xrange(2, int(math.sqrt(n)) + 1):
        if n % m == 0:
            sum += m
            if m < n / m:
                sum += n / m
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
        pivot_value = abundant_numbers[pivot_index]
    except IndexError:
        raise IndexError("idx: %s, len: %s, left: %s, right: %s" % (pivot_index, len(abundant_numbers), left, right))

    #~ print "  pivot_index: %s, pivot_value: %s " % (pivot_index, pivot_value)
    if sumand_1 + pivot_value == n:
        return True

    if right - left == 1:
        return False

    if sumand_1 + pivot_value > n:
        #~ print "  go left"
        return divide_conquer(n, sumand_1, abundant_numbers, left, pivot_index, depth + 1)
    else:
        #~ print "  go right"
        return divide_conquer(n, sumand_1, abundant_numbers, pivot_index, right, depth + 1)


def divide_array(the_array, count):
    """
        >>> divide_array(range(10), 3)
        [[0, 1, 2], [3, 4, 5], [6, 7, 8, 9]]

        >>> divide_array(range(11), 3)
        [[0, 1, 2], [3, 4, 5], [6, 7, 8, 9, 10]]

        >>> divide_array(range(12), 3)
        [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
    """
    retval = []
    slice_size = len(the_array) / count
    for n in range(count):
        retval.append(the_array[n * slice_size: (n + 1) * slice_size])

    rest = len(the_array) % count
    if rest != 0:
        retval[-1].extend(the_array[-rest:])
    return retval

def find_abundant_numbers(work_unit):
    """
        this is supposed to called from multiprocessing
    """
    print "find_abundant_numbers(%s..%s), start" % (work_unit[0], work_unit[-1])
    retval = []
    for n in work_unit:
        if is_abundant_naive(n):
            retval.append(n)
    #~ print "find_abundant_numbers(%s..%s), stop" % (work_unit[0], work_unit[-1])
    return retval

def find_sumands(work_unit):
    """
        this is supposed to called from multiprocessing
    """
    print "find_sumands(%s..%s), start" % (work_unit[1][0], work_unit[1][-1])
    sum = 0
    abundant_numbers = work_unit[0]
    for n in work_unit[1]:
        #~ lp.try_print("n: %s" % n)
        if not is_sum_of_abundant_numbers(n, abundant_numbers):
           sum += n
    return sum

def main():
    lp = LossyPrinter(1)
    total_watch = StopWatch()

    cpu_count = multiprocessing.cpu_count()
    #~ pool = multiprocessing.Pool(processes=cpu_count)
    #~ work_units = divide_array(range(max_n), cpu_count * 10)
#~
    #~ watch = StopWatch()
    #~ map_results = pool.map(find_abundant_numbers, work_units)
    #~ watch.print_time("Map")
#~
    #~ watch = StopWatch()
    abundant_numbers = []
    for n in xrange(max_n):
        if is_abundant_naive(n):
            abundant_numbers.append(n)

    #~ for item in map_results:
        #~ abundant_numbers.extend(item)
    #~ abundant_numbers = sorted(abundant_numbers)
    #~ watch.print_time("Reduce")

    #~ len(abundant_numbers): 6965
    print "len(abundant_numbers): %s"  % len(abundant_numbers)
    if len(abundant_numbers) < 100:
        print abundant_numbers

    #~ return

    pool = multiprocessing.Pool(processes=cpu_count)
    work_units = [(abundant_numbers, n) for n in divide_array(range(max_n), cpu_count * 2)]
    #~ find_sumands(work_units[0])
    watch = StopWatch()
    map_results = pool.map(find_sumands, work_units)
    watch.print_time("Map")

    sum = reduce(lambda x, y: x + y, map_results)

    #~ sum = 0
    #~ for n in range(max_n):
        #~ lp.try_print("n: %s" % n)
        #~ if not is_sum_of_abundant_numbers(n, abundant_numbers):
           #~ sum += n

    total_watch.print_time("Total")

    print "Anwser: %s" % sum
    # correct answer: 4179871
    if sum != 4179871:
        print "THIS IS INCORRECT!"



if __name__ == '__main__':
    failures, cnt_tests = doctest.testmod()
    if failures == 0:
        main()
