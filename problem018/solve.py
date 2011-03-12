from pprint import pprint

triangle = []

f = open('triangle_18.txt')
while True:
    line = f.readline()
    if line == "":
        break

    line = line.strip()
    numbers = line.split(' ')
    numbers = map(lambda x: int(x), numbers)
    triangle.append(numbers)

f.close()

triangle.reverse()
pprint(triangle)

for y, row in enumerate(triangle):
    if y == 0:
        continue

    for x, col in enumerate(row):
        if triangle[y - 1][x] > triangle[y - 1][x + 1]:
            triangle[y][x] = triangle[y - 1][x] + col
        else:
            triangle[y][x] = triangle[y - 1][x + 1] + col


pprint(triangle)
