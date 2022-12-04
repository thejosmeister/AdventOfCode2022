# Day 3 part 1
# quite a nice input to work with as can make a lot of assumptions
import string

import math

from common.common import parse_input_into_list_of_strings

bags = parse_input_into_list_of_strings("input.txt")

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
letters = lower + upper


def find_common_letter_score(x):
    first = set(list(x[:math.floor(len(x) / 2)]))
    second = set(list(x[math.floor(len(x) / 2):]))

    com = first.intersection(second)

    return letters.index(list(com)[0]) + 1


bag_scores = [find_common_letter_score(x) for x in bags]

print(sum(bag_scores))
