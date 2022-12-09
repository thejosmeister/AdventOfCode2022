# Day 8 part 2
# Cant read the question for this one
from common.common import parse_input_into_list_of_strings

rows = parse_input_into_list_of_strings("input.txt")

a = [[*x] for x in rows ]
grid = [ [int(z) for z in y] for y in a ]

v_trees = []


def calc_max_view_dist(i, j, param):
    global grid

    l_score = 0
    for a in range(i - 1, -1, -1):
        l_score += 1
        if grid[j][a] >= param:
            break

    r_score = 0
    for a in range(i + 1, len(grid[0])):
        r_score += 1
        if grid[j][a] >= param:
            break

    u_score = 0
    for a in range(j - 1, -1, -1):
        u_score += 1
        if grid[a][i] >= param:
            break

    d_score = 0
    for a in range(j + 1, len(grid)):
        d_score += 1
        if grid[a][i] >= param:
            break

    return l_score * r_score * u_score * d_score


for i in range(1, len(grid[0]) - 1):
    for j in range(1, len(grid) - 1):
        v_trees.append(calc_max_view_dist(i, j, grid[j][i]))

print(max(v_trees))