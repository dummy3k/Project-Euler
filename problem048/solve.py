
def lossy_add(current, add_this, max_value):
    """
        >>> lossy_add(1, 10, 100)
        11
        >>> lossy_add(1, 10, 10)
        1
        >>> lossy_add(2, 8, 10)
        10
    """
    retval = current + add_this
    if retval > max_value:
        retval -= max_value
    return retval

def lossy_multiply(alpha, beta, max_value):
    """
        >>> lossy_multiply(2, 3, 10)
        6
        >>> lossy_multiply(7, 3, 10)
        1
    """
    retval = 0
    for n in range(beta):
        retval = lossy_add(retval, alpha, max_value)
    return retval

def lossy_pow(alpha, beta, max_value):
    """
        >>> lossy_pow(2, 4, 100)
        16
        >>> lossy_pow(2, 4, 10)
        6
    """
    retval = alpha
    for n in range(beta - 1):
        retval = lossy_multiply(retval, alpha, max_value)
    return retval

max_value = 10000000000

def solve():
    import sys
    from euler_tools.misc import LossyPrinter

    lp = LossyPrinter(1)
    answer = 0
    #~ max_value = 10000000000
    for n in range(1000):
        lp.try_print(n)
        answer = lossy_add(answer, lossy_pow(n, n, max_value), max_value)

    print answer
    #~ 9110846700
    #~ 9110846700

def work(n):
    return lossy_pow(n, n, max_value)

def test_pool():
    from euler_tools.misc import StopWatch
    watch = StopWatch()

    import multiprocessing
    count = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=count)
    answers = pool.map(work, range(1000))

    answer = 0
    for item in answers:
        answer = lossy_add(answer, item, max_value)

    watch.print_time()
    print answer

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    #~ solve()
    test_pool()
