"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
import sys

number = 600851475143
#~ number = 13195

def kleinster_teiler(number):
    for n in xrange(2, sys.maxint-1):
        if number % n == 0:
            print "Teiler: %s" % n
            return n

    raise Exception("bad bad...")

while number > 1:
    teiler = kleinster_teiler(number)
    number /= teiler
