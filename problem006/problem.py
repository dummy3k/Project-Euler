
sum_of_squares = 0
squares_of_sum = 0

for n in range(1, 100 + 1):
    sum_of_squares += n**2
    squares_of_sum += n

squares_of_sum = squares_of_sum**2

print "sum_of_squares: %s" % sum_of_squares
print "squares_of_sum: %s" % squares_of_sum

difference = squares_of_sum - sum_of_squares
print "difference: %s" % difference
