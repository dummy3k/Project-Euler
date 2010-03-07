"""
Starting in the top left corner of a 2x2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?
"""

grid_size = 20


maxtrix = map(lambda x: map(lambda x: None, range(grid_size)), range(grid_size))

for x in range(grid_size):
    for y in range(grid_size):
        value = 0

        if x == 0:
            value += 1
        else:
            value += maxtrix[x - 1][y]

        if y == 0:
            value += 1
        else:
            value += maxtrix[x][y - 1]

        maxtrix[x][y] = value

print maxtrix
