#~ The following iterative sequence is defined for the set of positive integers:
#~
#~ n -> n/2 (n is even)
#~ n -> 3n + 1 (n is odd)
#~
#~ Using the rule above and starting with 13, we generate the following sequence:
#~ 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#~
#~ It can be seen that this sequence (starting at 13 and finishing at 1)
#~ contains 10 terms. Although it has not been proved yet (Collatz Problem),
#~ it is thought that all starting numbers finish at 1.
#~
#~ Which starting number, under one million, produces the longest chain?

def check_length(number):
    cnt = 1
    #~ number = 14
    while number != 1:
        #~ print number
        if number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1

        cnt += 1

    return cnt

max_length = 0
for n in range(1, 1000000):
    length = check_length(n)
    if length > max_length:
        print "n = %s, length = %s" % (n, length)
        max_length = length
