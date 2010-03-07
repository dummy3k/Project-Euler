"""
Starting in the top left corner of a 2x2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?
"""

grid_size = 4
visited = []

def step(x, y):
    #~ if (x, y) in visited:
        #~ print "Already visited %s, %s" % (x, y)
        #~ return

    if x == grid_size and y == grid_size:
        #~ print "Found solution"
        #~ solutions += 1
        return 1

    if x > grid_size or y > grid_size:
        return 0

    visited.append( (x, y) )
    #~ print "visit %s, %s" % (x, y)
    retval = 0
    retval += step(x + 1, y)
    retval += step(x, y + 1)
    return retval


solutions = step(0, 0)
print "solutions: %s" % solutions
