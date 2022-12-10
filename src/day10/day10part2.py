# Day 10 part 2
# Kind of fun, plenty of modulo
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
lines = [[] for i in range(6)]
line_no = 0

for i in range(0, 240):
    print(i, line_no)
    if i > 0 and i % 40 == 0:
        line_no += 1

    if value + 1 >= i % 40 >= value - 1:
        lines[line_no].append('#')
    else:
        lines[line_no].append('.')

    if instr[inst_index] == 0:
        inst_index += 1
        continue

    if cycle is True:
        value += instr[inst_index]
        inst_index += 1
        cycle = False
        continue

    cycle = True

for i in range(6):
    [print(x, end='') for x in lines[i]]
    print()






