"""
Surprisingly there are only three numbers that can be written as the sum
of fourth powers of their digits:

    1634 = 1^(4) + 6^(4) + 3^(4) + 4^(4)
    8208 = 8^(4) + 2^(4) + 0^(4) + 8^(4)
    9474 = 9^(4) + 4^(4) + 7^(4) + 4^(4)

As 1 = 1^(4) is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits.
"""

power_n = 5
solution_counter = 0
solution_sum = 0

for n in range(1000, 999999):
    digits = map(lambda x: int(x), str(n))
    sum = 0
    for digit in digits:
        sum += digit**power_n

    if sum == n:
        print "Found solution: %s" % n
        solution_counter += 1
        solution_sum += n

print "solution_counter: %s" % solution_counter
print "solution_sum: %s" % solution_sum
