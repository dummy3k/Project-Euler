import sys, os
from pprint import pprint

matrix = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331]
]


matrix = []
filename = os.path.join(os.path.dirname(__file__), 'matrix.txt')
f = open(filename, 'r')
while True:
    line = f.readline()
    if line == "":
        break
#~ #~
    matrix.append( map(lambda x: int(x), line.strip().split(',')) )
f.close()

rows = len(matrix)
cols = rows

#~ pprint(matrix, width=500)
pprint(matrix)
print "cols: %s, rows: %s" % (cols, rows)

def calc(x, y):
    #~ print "calc(%s, %s)" % (x, y)
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


#~ def calc2(x, y, score_map):



if __name__ == '__main__':
    score_map = [[None for n in range(cols)] for m in range(rows)]
    for y in range(rows - 1, -1, -1):
        for x in range(cols - 1, -1, -1):
            if x + 1 >= cols and y + 1 >= rows:
                score_map[x][y] = matrix[x][y]
            elif x + 1 >= cols:
                score_map[x][y] = matrix[x][y] + score_map[x][y + 1]
            elif y + 1 >= rows:
                score_map[x][y] = matrix[x][y] + score_map[x + 1][y]
            else:
                right_score = score_map[x + 1][y]
                down_score = score_map[x][y + 1]
#~ #~
                if right_score > down_score:
                    score_map[x][y] = matrix[x][y] + down_score
                else:
                    score_map[x][y] = matrix[x][y] + right_score

    #~ print calc(0, 0)
    pprint(score_map)
    print "Answer: %s" % score_map[0][0]

