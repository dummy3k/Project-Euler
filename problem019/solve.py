import datetime
#~ current = datetime.date(1901, 1, 1)
#~ while current < datetime.date(2000, 12, 31):

cnt = 0
for year in range(1901, 2000 + 1):
    for month in range(1, 12 + 1):
        current = datetime.date(year, month, 1)
        if current.weekday() == 6:
            print(current)
            cnt += 1


print "Count: %s" % cnt
