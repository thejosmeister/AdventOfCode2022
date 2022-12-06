# Day 5 part 1
# Fairly parse heavy which took up some time (I also can't read the question)
import re


def parse_input_into_list_of_strings2(input_file: str) -> list:
    input_list = []

    f = open(input_file, "r")

    for line in f:
        input_list.append(line.strip('\n'))

    f.close()

    return input_list


input_strings = parse_input_into_list_of_strings2("input.txt")

crate_info = []
move_info = []

add_crate_info = True

for l in input_strings:
    if l == '':
        add_crate_info = False
        continue
    if add_crate_info is True:
        crate_info.append(l)
        continue
    move_info.append(l)

# A faf to parse these
crate_states = [[] for i in range(9)]
j = 0
for i in range(1, 9 * 4 + 1, 4):
    for l in crate_info[:-1]:
        if l[i] != ' ':
            crate_states[j].append(l[i])
    j += 1

# first time cracking out the regex this year
moves = []
for l in move_info:
    groups = re.search("move ([0-9]+) from ([0-9]+) to ([0-9]+)", l)
    moves.append([int(groups.group(1)), int(groups.group(2)), int(groups.group(3))])

# I guess each crate is some sort of fifo but lists will do
for move in moves:
    m = crate_states[move[1] - 1][:move[0]]
    # did not read the q properly and left this out
    m.reverse()
    crate_states[move[2] - 1] = m + crate_states[move[2] - 1]
    crate_states[move[1] - 1] = crate_states[move[1] - 1][move[0]:]

for c in crate_states:
    print(c[0], end="")
