import doctest


def word_value(s):
    """
        >>> word_value('SKY')
        55
    """
    retval = 0
    for item in s:
        retval += ord(item) - 64
    return retval
    
def main():
    with open('words.txt') as f:
        buffer = f.read()

    buffer = buffer.replace('"', '')
    #~ print buffer
    words = buffer.split(',')
    #~ print words
    max_value = 0
    for item in words:
        max_value = max(max_value, word_value(item))

    print "max_value: %s" % max_value
    n = 1
    t = 0
    triangle_numbers = []
    while t < max_value:
        t = 0.5 * n * (n + 1)
        triangle_numbers.append(int(t))
        #~ print "%s\t%s" % (n, t)
        n += 1

    print "triangle_numbers: %s" % triangle_numbers

    cnt = 0
    for item in words:
        if word_value(item) in triangle_numbers:
            cnt += 1

    print "anwer: %s" % cnt
    
if __name__ == '__main__':
    doctest.testmod()
    main()
