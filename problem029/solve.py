max_n = 100

terms = []
for a in range(2, max_n + 1):
    for b in range(2, max_n + 1):
        value = a ** b
        if not value in terms:
            terms.append(value)

print "Anwser: %s" % len(terms)
