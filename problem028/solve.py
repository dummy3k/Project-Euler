edge_size = 1001
field = [[None for n in range(edge_size)] for m in range(edge_size)]

x = edge_size / 2
y = edge_size / 2
steps = 1
steps_rest = 2

# 0 right
# 1 down
# 2 left
# 3 up
direction = 0

#~ for n in range(1, 26):
n = 0
while x < edge_size and y < edge_size:
    n += 1
    field[y][x] = n
    steps_rest -= 1

    if steps_rest <= 0:
        direction += 1
        direction %= 4

        if direction == 0 or direction == 2:
            steps += 1

        steps_rest = steps

    if direction == 0:
        x += 1
    elif direction == 1:
        y += 1
    elif direction == 2:
        x -= 1
    elif direction == 3:
        y -= 1

def print_field():
    col_width = 5
    for y in range(edge_size):
        row = ""
        for x in range(edge_size):
            if field[y][x]:
                row += "|%5i" % field[y][x]
            else:
                row += '|' + ' ' * col_width
        print(row)

#~ print_field()

sum = 0
for n in range(edge_size):
    sum += field[n][n]
    if n != edge_size - n - 1:
        sum += field[n][edge_size - n - 1]

print "Anweser: %s" % sum
