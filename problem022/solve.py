from pprint import pprint

with open("names.txt") as f:
    line = f.readline()

line = line.replace('"', '')
names = line.split(',')

names.sort()

def get_value(s):
    """
        >>> get_value('COLIN')
        53
    """
    retval = 0
    for c in s:
        retval += ord(c) - 64

    return retval

if __name__ == '__main__':
    import doctest
    doctest.testmod()

answer = 0
for index, item in enumerate(names):
    answer += get_value(item) * (index + 1)

print("Anwser: %s" % answer)
#~ pprint(names)
