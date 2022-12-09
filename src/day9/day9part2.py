# Day 9 part 2
# All done before car passed its MOT
from common.common import parse_input_into_list_of_strings

rows = parse_input_into_list_of_strings("input.txt")

instructions = [[x.split(' ')[0],int(x.split(' ')[1])] for x in rows]

knots = [[0,0] for i in range(10)]

t_poses = ["0,0"]


def move_head(i):
    global knots
    if i == 'L':
        knots[0][0] -= 1
    if i == 'R':
        knots[0][0] += 1
    if i == 'D':
        knots[0][1] += 1
    if i == 'U':
        knots[0][1] -= 1


def move_tail(knot):
    global knots
    global t_poses

    x_diff = knots[knot - 1][0] - knots[knot][0]
    y_diff = knots[knot - 1][1] - knots[knot][1]

    if x_diff > 1:
        knots[knot][0] += 1
        if y_diff > 0:
            knots[knot][1] += 1
        if y_diff < 0:
            knots[knot][1] -= 1

        if knot == 9:
            if f"{knots[knot][0]},{knots[knot][1]}" not in t_poses:
                t_poses.append(f"{knots[knot][0]},{knots[knot][1]}")

        return

    if x_diff < -1:
        knots[knot][0] -= 1
        if y_diff > 0:
            knots[knot][1] += 1
        if y_diff < 0:
            knots[knot][1] -= 1
        if knot == 9:
            if f"{knots[knot][0]},{knots[knot][1]}" not in t_poses:
                t_poses.append(f"{knots[knot][0]},{knots[knot][1]}")

        return

    if y_diff < -1:
        knots[knot][1] -= 1
        if x_diff > 0:
            knots[knot][0] += 1
        if x_diff < 0:
            knots[knot][0] -= 1

        if knot == 9:
            if f"{knots[knot][0]},{knots[knot][1]}" not in t_poses:
                t_poses.append(f"{knots[knot][0]},{knots[knot][1]}")

        return

    if y_diff > 1:
        knots[knot][1] += 1
        if x_diff > 0:
            knots[knot][0] += 1
        if x_diff < 0:
            knots[knot][0] -= 1

        if knot == 9:
            if f"{knots[knot][0]},{knots[knot][1]}" not in t_poses:
                t_poses.append(f"{knots[knot][0]},{knots[knot][1]}")

        return


for i in instructions:
    for j in range(i[1]):
        move_head(i[0])
        for n in range(1,10):
            move_tail(n)

print(len(t_poses))
