# Day 10 part 1
# Clunky soln but pretty easy
from common.common import parse_input_into_list_of_strings

rows = parse_input_into_list_of_strings("input.txt")


def parse_instr(x):
    if x == 'noop':
        return 0
    return int(x.split(' ')[1])


instr = [parse_instr(x) for x in rows]

value = 1
inst_index = 0
cycle = False
strengths = []
for i in range(1,221):
    if i % 40 == 20:
        strengths.append(i * value)
    if instr[inst_index] == 0:
        inst_index += 1
        continue

    if cycle is True:
        value += instr[inst_index]
        inst_index += 1
        cycle = False
        continue

    cycle = True


print(sum(strengths))




