# Day 14 part 1
# Pretty fun one, had to correct what I was doing at x = 500
from common.common import parse_input_into_list_of_strings, flatten_list

lines = parse_input_into_list_of_strings("input.txt")

line_points = []
for line in lines:
    points = [l.split(',') for l in line.split(' -> ')]
    line_points.append([[int(p[0]), int(p[1])] for p in points])

max_x = max(flatten_list([[p[0] for p in l] for l in line_points]))
max_y = max(flatten_list([[p[1] for p in l] for l in line_points]))
min_x = min(flatten_list([[p[0] for p in l] for l in line_points]))

# put the grid together
grid = []

for i in range(max_y + 1):
    grid.append([])
    for j in range(max_x + 1):
        grid[i].append('.')

for point_set in line_points:
    for i in range(len(point_set) - 1):
        x1 = point_set[i][0]
        x2 = point_set[i + 1][0]
        y1 = point_set[i][1]
        y2 = point_set[i + 1][1]
        if x1 != x2:
            # horizontal
            for j in range(min(x1, x2), max(x1, x2) + 1):
                grid[y1][j] = '#'
        else:
            # vertical
            for j in range(min(y1, y2), max(y1, y2) + 1):
                grid[j][x1] = '#'


y = 0
while True:
    if grid[y][500] == '#':
        break
    y += 1

initial_point = [500, y]
current_point = initial_point.copy()


def observe_point(point):
    if grid[point[1]][point[0]] == '.':
        return [point[0], point[1] + 1]

    if grid[point[1]][point[0] - 1] == '.':
        return [point[0] - 1, point[1] + 1]

    if grid[point[1]][point[0] + 1] == '.':
        return [point[0] + 1, point[1] + 1]

    return [-1, -1]



def add_sand():
    global current_point
    global grid

    rtn_val = True
    p = current_point.copy()
    while True:
        val = observe_point(p)
        if val == [-1, -1]:
            grid[p[1] - 1][p[0]] = 'O'
            break
        if val[1] >= len(grid):
            rtn_val = False
            break
        p = val

    if p == current_point:
        current_point = [p[0], p[1] - 1]
    return rtn_val


while True:
    if add_sand() is False:
        break

sand_count = 0

for r in grid:
    sand_count += len(list(filter(lambda x: x == 'O', r)))

print(sand_count)

# a pretty picture for everyone
for y in grid:
    for x in range(len(y)):
        if x >= min_x - 1:
            print(y[x], end='')
    print()

