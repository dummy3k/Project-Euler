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
#~ 0123
#~ 0132
#~ 0213
#~ 0231
#~ 0312
#~ 0321


def next_number(digits):
    #~ digits = map(lambda x: int(x), str(number))
    move_this = digits.pop()
    for n in range(len(digits) - 1, -1, -1):
        if move_this > digits[n]:
            digits.insert(n, move_this)
            break

    return digits



current = [0, 1, 2]
for n in range(5):
    print current
    current = next_number(current)
