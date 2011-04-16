from euler_tools.misc import StopWatch, LossyPrinter

lp = LossyPrinter(1)

def is_abundant(n):
    sum = 0
    for m in range(1, n):
        if n % m == 0:
            sum += m
            if sum > n:
                return True

    return (sum > n)

max_n = 28123
#~ max_n = 5000
abundant_numbers = []
for n in range(max_n):
    lp.try_print(n)
    if is_abundant(n):
        abundant_numbers.append(n)

print "len(abundant_numbers): %s"  % len(abundant_numbers)
if len(abundant_numbers) < 100:
    print abundant_numbers

candidates = range(max_n)
for index, n in enumerate(abundant_numbers):
    for m in abundant_numbers[index:]:
        local_sum = n + m
        if local_sum < max_n:
            #~ lp.try_print("%s + %s = %s" % (n, m, local_sum))
            if local_sum in candidates:
                lp.try_print("%s + %s = %s, removed" % (n, m, local_sum))
                candidates.remove(local_sum)

print "len(candidates): %s" % len(candidates)

sum = reduce(lambda x, y: x + y, candidates)
print "Anwser: %s" % sum

# correct answer: 4179871
