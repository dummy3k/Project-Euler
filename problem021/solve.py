
def fn_d(n):
    """
        >>> fn_d(220)
        284
        >>> fn_d(284)
        220
    """
    retval = 0
    for divisor in range(1, n):
        if n % divisor == 0:
            retval += divisor
    return retval

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    from euler_tools.misc import StopWatch
    watch = StopWatch()

    max_n = 10000
    sum = 0
    for n in range(max_n):
        result = fn_d(n)
        if result != n:
            if fn_d(result) == n:
                sum += n

    watch.print_time()
    print sum
