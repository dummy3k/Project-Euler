from euler_tools.misc import is_palindrome

sum = 0
for n in range(1, 1000000):
#~ for n in range(1, 100):
    if is_palindrome(n):
        binary_string = bin(n)[2:]
        if is_palindrome(binary_string):
            print "%s\t%s"  % (n, binary_string)
            sum += n

print "Answer: %s" % sum


