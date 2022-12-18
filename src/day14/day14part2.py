# Day 14 part 2
# Just went with a bigger grid, looks like I didn't need any logic for adding columns to the left
from common.common import parse_input_into_list_of_strings, flatten_list

lines = parse_input_into_list_of_strings("input.txt")

line_points = []
for line in lines:
    points = [l.split(',') for l in line.split(' -> ')]
    line_points.append([[int(p[0]), int(p[1])] for p in points])

max_x = max(flatten_list([[p[0] for p in l] for l in line_points]))
max_y = max(flatten_list([[p[1] for p in l] for l in line_points]))
min_x = min(flatten_list([[p[0] for p in l] for l in line_points]))

grid = []

for i in range(max_y + 2):
    grid.append([])
    for j in range(max_x + 1):
        grid[i].append('.')
grid.append([])
for j in range(max_x + 1):
    grid[max_y + 2].append('#')

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
            if p[1] - 1 == 0:
                rtn_val = False
            break
        if val[0] >= len(grid[0]) - 1:
            for g in grid:
                g.append('.')
                g.append('.')
            grid[-1][-1] = '#'
            grid[-1][-2] = '#'
        if val[0] < 0:
            for g in grid:
                g.insert(0, '.')
                g.insert(0, '.')
            grid[-1][0] = '#'
            grid[-1][1] = '#'

            val = [val[0] + 2, val[1]]
            current_point = [current_point[0] + 2, current_point[1]]
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

# A bigger pretty picture
for y in grid:
    for x in range(len(y)):
        if x > 320:
            print(y[x], end='')
    print()
