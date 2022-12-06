# Day 6 part 1
# nothing too funky today
from common.common import parse_input_into_list_of_strings

line = parse_input_into_list_of_strings("input.txt")[0]

for i in range(len(line)-4):
    if len(list(set(line[i:i+4]))) == 4:
        print(i+4)
        break
