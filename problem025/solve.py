from euler_tools.misc import fib

idx = 0
for n in fib():
    idx += 1
    if len(str(n)) >= 1000:
        print idx
        break
