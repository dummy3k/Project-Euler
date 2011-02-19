from pprint import pprint

matrix = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331]
]
rows = len(matrix)
cols = rows

pprint(matrix)

def calc(x, y):
    print "calc(%s, %s)" % (x, y)
    retval = matrix[x][y]

    if x + 1 >= cols and y + 1 >= rows:
        return retval

    if x + 1 < cols:
        go_right = calc(x + 1, y)
        if y + 1 >= rows:
            return retval + go_right

    if y + 1 < rows:
        go_down = calc(x, y + 1)
        if x + 1 >= cols:
            return retval + go_down

    if go_right < go_down:
        return retval + go_right
    else:
        return retval + go_down


print calc(0, 0)
