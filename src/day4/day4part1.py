# Day 4 part 1
# had a small frustration when I realised I hadn't parsed the strings to ints
# (who would have known that strong typing was useful)
from common.common import parse_input_into_list_of_strings, flatten_list


def parse_range(x: str):
    strings = flatten_list([y.split("-") for y in x.split(",")])
    return [int(y) for y in strings]


ranges = parse_input_into_list_of_strings("input.txt")
split_ranges = [parse_range(x) for x in ranges]

count = len(list(filter(lambda x: ((x[0] >= x[2] and x[1] <= x[3]) or (x[0] <= x[2] and x[1] >= x[3])), split_ranges)))

print(count)
