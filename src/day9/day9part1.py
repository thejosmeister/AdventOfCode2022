# Day 9 part 1
# Feel like this one was the first properly fun one
from common.common import parse_input_into_list_of_strings

rows = parse_input_into_list_of_strings("input.txt")

instructions = [[x.split(' ')[0],int(x.split(' ')[1])] for x in rows]

h_pos = [0,0]
t_pos = [0,0]

t_poses = ["0,0"]


def move_head(i):
    global h_pos
    if i == 'L':
        h_pos[0] -= 1
    if i == 'R':
        h_pos[0] += 1
    if i == 'D':
        h_pos[1] += 1
    if i == 'U':
        h_pos[1] -= 1


def move_tail():
    global h_pos
    global t_pos
    global t_poses

    x_diff = h_pos[0] - t_pos[0]
    y_diff = h_pos[1] - t_pos[1]

    if x_diff > 1:
        t_pos[0] += 1
        if y_diff > 0:
            t_pos[1] += 1
        if y_diff < 0:
            t_pos[1] -= 1

        if f"{t_pos[0]},{t_pos[1]}" not in t_poses:
            t_poses.append(f"{t_pos[0]},{t_pos[1]}")

        return

    if x_diff < -1:
        t_pos[0] -= 1
        if y_diff > 0:
            t_pos[1] += 1
        if y_diff < 0:
            t_pos[1] -= 1

        if f"{t_pos[0]},{t_pos[1]}" not in t_poses:
            t_poses.append(f"{t_pos[0]},{t_pos[1]}")

        return

    if y_diff < -1:
        t_pos[1] -= 1
        if x_diff > 0:
            t_pos[0] += 1
        if x_diff < 0:
            t_pos[0] -= 1

        if f"{t_pos[0]},{t_pos[1]}" not in t_poses:
            t_poses.append(f"{t_pos[0]},{t_pos[1]}")

        return

    if y_diff > 1:
        t_pos[1] += 1
        if x_diff > 0:
            t_pos[0] += 1
        if x_diff < 0:
            t_pos[0] -= 1

        if f"{t_pos[0]},{t_pos[1]}" not in t_poses:
            t_poses.append(f"{t_pos[0]},{t_pos[1]}")

        return


for i in instructions:
    for j in range(i[1]):
        move_head(i[0])
        move_tail()

print(len(t_poses))
