# Day 13 part 1
# Original work on this was lost when I threw water over my laptop so had to start again
from common.common import parse_input_into_list_of_strings

rows = parse_input_into_list_of_strings("input.txt")

pairs = []

for i in range(0, len(rows), 3):
    x = []
    y = []

    exec("x = " + rows[i])
    exec("y = " + rows[i + 1])

    pairs.append([x, y])

right_pairs = []


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


def determine_if_right(pair):
    left = pair[0]
    right = pair[1]

    a = compare_lists(left, right)
    print(f"{left}    {right}")
    print(a)
    print()

    return a > 1


for pair in pairs:
    if determine_if_right(pair) is True:
        right_pairs.append(pairs.index(pair) + 1)

print(sum(right_pairs))
