from euler_tools.misc import find

def written_number(n):
    """
        >>> written_number(1)
        'one'
        >>> written_number(10)
        'ten'

        These are special
        >>> written_number(11)
        'eleven'
        >>> written_number(12)
        'twelve'
        >>> written_number(13)
        'thirteen'

        This ends with "teen"
        >>> written_number(14)
        'fourteen'

        this is special
        >>> written_number(15)
        'fifteen'

        All follwing end with teen
        >>> written_number(16)
        'sixteen'
        >>> written_number(17)
        'seventeen'
        >>> written_number(18)
        'eightteen'
        >>> written_number(19)
        'nineteen'

        >>> written_number(20)
        'twenty'
        >>> written_number(21)
        'twenty one'
        >>> written_number(29)
        'twenty nine'

        >>> written_number(30)
        'thirty'

        >>> written_number(35)
        'thirty five'

        >>> written_number(81)
        'eighty one'

        >>> written_number(98)
        'ninety eight'

        >>> written_number(100)
        'one hundred'

        >>> written_number(300)
        'three hundred'

        >>> written_number(342)
        'three hundred and forty two'

        >>> written_number(115)
        'one hundred and fifteen'

        >>> written_number(1000)
        'one thousand'
    """
    one_digit_words = ['zero', 'one', 'two', 'three', 'four', 'five',
                       'six', 'seven', 'eight', 'nine']
    if n < 10:
        return one_digit_words[n]

    if n in [10, 11, 12, 13, 15, 18]:
        specials = [(10, 'ten'), (11, 'eleven'), (12, 'twelve'),
                    (13, 'thirteen'), (15, 'fifteen'), (18, 'eighteen')]
        return find(lambda x: x[0] == n, specials)[1]

    if n < 20:
        return one_digit_words[n % 10] + 'teen'

    two_digits_words = [None, None, 'twenty', 'thirty', 'forty',
                        'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if n < 100:
        if n % 10 == 0:
            return two_digits_words[n / 10]

        return two_digits_words[n / 10] + ' ' + one_digit_words[n % 10]

    if n < 1000:
        if n % 100 == 0:
            return one_digit_words[n / 100] + ' hundred'

        return one_digit_words[n / 100] + ' hundred and ' + written_number(n % 100)

    return 'one thousand'

def count_letters(n):
    """
        >>> count_letters(342)
        23
        >>> count_letters(115)
        20
    """
    return len(written_number(n).replace(' ', ''))

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    sum = 0
    for n in range(1, 1001):
        sum += count_letters(n)
        #~ print "%s\t%s" % (n, written_number(n))

    print sum
