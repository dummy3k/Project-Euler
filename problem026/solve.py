import doctest

class NoCycleError(Exception):
    pass
    
def cycle_length(d, do_log=False):
    """
        >>> cycle_length(6)
        1
        >>> cycle_length(7)
        6
        >>> cycle_length(8)
        Traceback (most recent call last):
        NoCycleError
    """
    
    visited_digits = []
    n = 1
    while True:
        if n in visited_digits:
            return len(visited_digits) - visited_digits.index(n)
        visited_digits.append(n)

        while n < d:
            n *= 10
            
        digit = n / d
        rest = n % d
        if do_log:
            print "%s\t:%s = %s\tR %s" % (n, d, digit, rest)

        if rest == 0:
            raise NoCycleError()
            
        n = rest

    return None
    
    #~ 1   :   7   = 0 R 7
    #~ 10  :   7   = 1 R 3
    #~ 30  :   7   = 4 R 2
    #~ 20  :   7   = 2 R 6
    #~ 60  :   7   = 8 R 4
    #~ 40  :   7   = 5 R 5
    #~ 50  :   7   = 7 R 1
    #~ 10  --> repeating

#~ print cycle_length(13, True)

def main():
    max_length = 0
    for d in range(1, 1001):
        try:
            length = cycle_length(d)
            if length > max_length:
                print "%s -> %s" % (d, length)
                max_length = length
                
        except NoCycleError:
            pass
            
if __name__ == '__main__':
    doctest.testmod()
    main()
