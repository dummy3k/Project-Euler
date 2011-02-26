
def fak(n):
    if n == 1:
        return 1

    return n * fak(n -1)

rest = fak(100)
answer = 0
while rest > 0:
    answer += rest % 10
    rest /=10

print answer
