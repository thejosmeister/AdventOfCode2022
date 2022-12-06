# Day 6 part 2
# Suspiciously easy, maybe we are in for a hard one tomorrow
from common.common import parse_input_into_list_of_strings

line = parse_input_into_list_of_strings("input.txt")[0]

for i in range(len(line)-14):
    if len(list(set(line[i:i+14]))) == 14:
        print(i+14)
        break