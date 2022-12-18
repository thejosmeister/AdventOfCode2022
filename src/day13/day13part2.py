# Day 13 part 2
# Pretty quick job to add a rudimentary bubble sort
from common.common import parse_input_into_list_of_strings

rows = parse_input_into_list_of_strings("input.txt")

stuff = []

for i in range(0, len(rows), 3):
    x = []
    y = []

    exec("x = " + rows[i])
    exec("y = " + rows[i + 1])

    stuff.append(x)
    stuff.append(y)

right_pairs = []
two = [[2]]
six = [[6]]
stuff.append(two)
stuff.append(six)


def compare_lists(left, right):
    if len(left) == 0:
        if len(right) == 0:
            return 1
        return 2
    elif len(right) == 0:
        return -1

    l_int = isinstance(left[0], int)
    r_int = isinstance(right[0], int)

    if l_int is True and r_int is True:
        if left[0] < right[0]:
            return 2
        if left[0] > right[0]:
            return -1
        return 1 * compare_lists(left[1:], right[1:])

    if l_int is True:
        c = compare_lists([left[0]], right[0])
        if c == 1:
            return compare_lists(left[1:], right[1:])
        return c

    if r_int is True:
        c = compare_lists(left[0], [right[0]])
        if c == 1:
            return compare_lists(left[1:], right[1:])
        return c

    # both lists
    d = compare_lists(left[0], right[0])
    if d == 1:
        return compare_lists(left[1:], right[1:])
    return d


keep_checking = True

while keep_checking is True:
    x = 0
    for i in range(len(stuff) - 1):
        r = compare_lists(stuff[i], stuff[i + 1])
        if r < 1:
            # nasty looking
            x += 1
            t = stuff[i].copy()
            stuff[i] = stuff[i + 1]
            stuff[i + 1] = t

    if x == 0:
        keep_checking = False

right_pairs.append(stuff.index(two) + 1)
right_pairs.append(stuff.index(six) + 1)

print(right_pairs[0] * right_pairs[1])
