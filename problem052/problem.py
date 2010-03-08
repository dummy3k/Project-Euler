"""
It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""

def test(digits, factor):
    digits2 = map(lambda x: int(x), str(n * factor))
    digits2.sort()
    if digits != digits2:
        return False

    return True

#~ for n in xrange(125874+10):
n = 0
max_factor = 6
while True:
    n += 1
    digits = map(lambda x: int(x), str(n))
    digits.sort()

    success = True
    msg = "%s\t" % n
    for m in range(max_factor, 0, -1):
    #~ for m in [5, 6]:
        if not test(digits, m):
            success = False
            break
        msg += "%s\t" % (n * m)

    if not success:
        continue


    print msg
    #~ print n, n * 2
print "Finished"
