# Day 4 part 2
# Quite brute forcey putting into ranges and sets but feels like less typing (I am the critical path in all my work)
from common.common import parse_input_into_list_of_strings, flatten_list


def parse_range(x: str):
    strings = flatten_list([y.split("-") for y in x.split(",")])
    ints = [int(y) for y in strings]
    return [[i for i in range(ints[0], ints[1] + 1)], [i for i in range(ints[2], ints[3] + 1)]]


ranges = parse_input_into_list_of_strings("input.txt")
split_ranges = [parse_range(x) for x in ranges]

count = len(list(filter(lambda x: (len(set(x[0]).intersection(set(x[1]))) > 0), split_ranges)))

print(count)
