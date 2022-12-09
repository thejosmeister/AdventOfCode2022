# Day 8 part 1
# Was pretty fun, took me a while to work out where i was meant to reset the tallest tree
from common.common import parse_input_into_list_of_strings

rows = parse_input_into_list_of_strings("input.txt")

a = [[*x] for x in rows ]
grid = [ [int(z) for z in y] for y in a ]

v_trees = []


for i in range(len(grid[0])):
    tallest = -1
    for j in range(len(grid)):
        if grid[j][i] > tallest:
            if f"{i},{j}" not in v_trees:
                v_trees.append(f"{i},{j}")
            tallest = grid[j][i]


for j in range(len(grid)):
    tallest = -1
    for i in range(len(grid[0])):
        if grid[j][i] > tallest:
            if f"{i},{j}" not in v_trees:
                v_trees.append(f"{i},{j}")
            tallest = grid[j][i]


for i in range(len(grid[0])):
    tallest = -1
    for j in range(len(grid)-1, -1, -1):
        if grid[j][i] > tallest:
            if f"{i},{j}" not in v_trees:
                v_trees.append(f"{i},{j}")
            tallest = grid[j][i]


for j in range(len(grid)):
    tallest = -1
    for i in range(len(grid[0])-1, -1, -1):
        if grid[j][i] > tallest:
            if f"{i},{j}" not in v_trees:
                v_trees.append(f"{i},{j}")
            tallest = grid[j][i]

print(len(v_trees))