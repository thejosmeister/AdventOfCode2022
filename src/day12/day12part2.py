# Day 12 part 2
# Im not actually sure how my solns worked in the end as I removed some logic which I thought was necessary but stopped it working.
import string

from common.common import parse_input_into_list_of_strings

rows = parse_input_into_list_of_strings("input.txt")

grid = [[*x] for x in rows]

start_pos = [0, 0]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "E":
            start_pos = [j, i]

shortest_dists = {"E": 0}
shortest_dists_to_p = {f"{start_pos[0]},{start_pos[1]}": 0}

MAX = 1000000000


def height_of(param):
    if param == 'E':
        return 25
    if param == "S":
        return 0
    return string.ascii_lowercase.index(param)


def find_shortest(i, j, height, length):
    if "a" in shortest_dists:
        if length > shortest_dists["a"]:
            return MAX
    elif length > 950:
        return MAX

    if grid[j][i] == "a":
        shortest_dists["a"] = length
        return length

    current_pos = [i, j]
    shortests = []

    for x in [[current_pos[0], current_pos[1] + 1], [current_pos[0], current_pos[1] - 1],
              [current_pos[0] + 1, current_pos[1]], [current_pos[0] - 1, current_pos[1]]]:
        if len(grid) > x[1] >= 0 and 0 <= x[0] < len(grid[0]):
            if height_of(grid[x[1]][x[0]]) >= height - 1: # doesnt work if I place upper bound??
                if f"{x[0]},{x[1]}" in shortest_dists_to_p:
                    if shortest_dists_to_p[f"{x[0]},{x[1]}"] > length + 1:
                        shortest_dists_to_p[f"{x[0]},{x[1]}"] = length + 1
                        shortest_dists_to_p[f"{x[0]},{x[1]}"] = length + 1
                        shortests.append(find_shortest(x[0], x[1], height_of(grid[x[1]][x[0]]), length + 1))
                    else:
                        shortests.append(MAX)
                else:
                    shortest_dists_to_p[f"{x[0]},{x[1]}"] = length + 1
                    shortests.append(find_shortest(x[0], x[1], height_of(grid[x[1]][x[0]]), length + 1))
            else:
                shortests.append(MAX)
        else:
            shortests.append(MAX)

    if min(shortests) == MAX:
        return MAX

    else:
        return min(shortests)


print(find_shortest(start_pos[0], start_pos[1], 25, 0))
