"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which, a^(2) + b^(2) = c^(2)

For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

found_solution = False

for a in range(1, 1000):
    for b in range(1, 1000 - a):
        c = 1000 - a - b
        #~ print "%s + %s + %s" % (a, b, c)
        if a**2 + b**2 == c**2:
            print "Found triple: %s^2 + %s^2 = %s^2" % (a, b, c)
            found_solution = True
            break

        if found_solution:
            break

    if found_solution:
        break


print "found_solution " + str(found_solution)
print a * b * c
