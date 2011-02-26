from euler_tools.misc import fib

sum = 0
for n in fib(4000000):
    if n % 2 == 0:
        sum += n

print sum
