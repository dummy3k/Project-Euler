"""
2^(15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^(1000)?
"""

"""
n	2^n
0	    1
1	    2
2	    4
3	    8
4	   16
5	   32
6	   64
7 	  128
8	  256
9	  512
10	 1024
11	 2048
12	 4096
13	 8192
14	16384
15	32768
"""

# an array of the resulting number. In reverse order, because it is
# easier to append to the tail.
result = [1]
power_n = 5

def double_it(s):
    retval = []
    for
#~ for n in range(1, power_n + 1):
    #~ for m in range(len(result)):
        #~ tmp = result[m] * 2
        #~ result[m] = tmp % 10
        #~ if tmp > 10:
            #~ if m + 1 == len(result):
                #~ result.append(1)
            #~ else:
                #~ result[m + 1] += 1

result.reverse()
result_str = reduce(lambda x, y: x + str(y), result, "")
print "result_str: %s" % result_str
