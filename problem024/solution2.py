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


max_digit = 9

def is_ok(number):
    digits = map(lambda x: int(x), str(number))
    for m in digits:
        if m > max_digit:
            return False

    for n in range(max_digit + 1):
        if n == 0 and len(digits) == max_digit:
            continue

        if not n in digits:
            return False


    return True

number = 123456789
for n in range(20):
    number += 1
    while not is_ok(number):
        number += 1

    print "solution: %s, number:\t%s" % (n, number)
    #~ if number > 99999:
        #~ break
