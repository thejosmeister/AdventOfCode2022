# Day 12 part 1
# Couldn't find a route finding thing from previous years, this one is a bit dirty
import string

from common.common import parse_input_into_list_of_strings

rows = parse_input_into_list_of_strings("input.txt")

grid = [[*x] for x in rows]

# why do I do this stuff in such a weird way?
start_pos = [0, list(filter(lambda j: grid[j][0] == "S", [i for i in range(len(grid))]))[0]]
end_pos = [list(filter(lambda j: grid[start_pos[1]][j] == "E", [i for i in range(len(grid[0]))]))[0], start_pos[1]]
shortest_dists = {f"0,{start_pos[1]}": 0}

MAX = 1000000000


def height_of(param):
    if param == 'E':
        return 25
    if param == "S":
        return 0
    return string.ascii_lowercase.index(param)


def find_shortest(i, j, height, length):
    if f"{end_pos[0]},{end_pos[1]}" in shortest_dists:
        if length > shortest_dists[f"{end_pos[0]},{end_pos[1]}"]:
            return MAX
    elif length > 950:
        return MAX

    if grid[j][i] == "E":
        shortest_dists[f"{end_pos[0]},{end_pos[1]}"] = length
        return length

    current_pos = [i, j]

    shortests = []

    for x in [[current_pos[0], current_pos[1] + 1], [current_pos[0], current_pos[1] - 1],
              [current_pos[0] + 1, current_pos[1]], [current_pos[0] - 1, current_pos[1]]]:

        if len(grid) > x[1] >= 0 and 0 <= x[0] < len(grid[0]):
            if height_of(grid[x[1]][x[0]]) <= height + 1:
                if f"{x[0]},{x[1]}" in shortest_dists:
                    if shortest_dists[f"{x[0]},{x[1]}"] > length + 1:
                        shortest_dists[f"{x[0]},{x[1]}"] = length + 1
                        shortests.append(find_shortest(x[0], x[1], height_of(grid[x[1]][x[0]]), length + 1))
                    else:
                        shortests.append(MAX)
                else:
                    shortest_dists[f"{x[0]},{x[1]}"] = length + 1
                    shortests.append(find_shortest(x[0], x[1], height_of(grid[x[1]][x[0]]), length + 1))
            else:
                shortests.append(MAX)
        else:
            shortests.append(MAX)

    if min(shortests) == MAX:
        return MAX

    else:
        return min(shortests)


print(find_shortest(0, start_pos[1], 0, 0))
