"""
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
if __name__ == "__main__":
    import sys, os
    sys.path.append( os.path.join( os.getcwd(), '..' ) )

from euler_tools.misc import is_palindrome

digits = 2

min_value = 100
max_value = 999

#~ print "is_palindrome(11): " % is_palindrome(11)
#~ print is_palindrome(12321)

solution_found = False
solution = None
for n in range(max_value, min_value, -1):
    for m in range(max_value, min_value, -1):
        product = n * m
        if is_palindrome(product):
            if not solution or product > solution:
                print "%s * %s = %s" % (n, m, product)
                solution = product
            #~ solution_found = True
            #~ break


    if solution_found:
        break
