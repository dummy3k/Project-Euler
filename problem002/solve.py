
def fib(max=None):
    alpha = 1
    yield alpha

    beta = 2
    yield beta

    while True:
        tmp = alpha + beta
        alpha = beta
        beta = tmp
        if beta > max:
            return

        yield beta


sum = 0
for n in fib(4000000):
    if n % 2 == 0:
        sum += n

print sum
