"""
A permutation is an ordered arrangement of objects. For example, 3124 is
one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the
digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""


#~ 01
#~ 10
#~
#~ 012
#~ 021
#~ 102
#~ 120
#~ 210
#~
#~ 0123     swap
#~ 0132
#~ 0213     swap
#~ 0231
#~ 0312
#~ 0321

try:
    import euler_tools
except ImportError:
    print "Hacked!"
    import sys, os
    sys.path.append( os.path.join( os.getcwd(), '..' ) )

from euler_tools.permutation import next_number

def as_string(sequence):
    return reduce(lambda x, y: x + str(y), sequence, "")


start_digits = map(lambda x: int(x), str("0123456789"))
print "start_digits:\t%s" % as_string(start_digits)

current = start_digits
for n in range(1000000 - 1):
    current = next_number(current)
print "current:\t%s" % as_string(current)
