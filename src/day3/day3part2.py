# Day 3 part 2
# my soln to part 1 made this pretty quick
import string

from common.common import parse_input_into_list_of_strings

bags = parse_input_into_list_of_strings("input.txt")

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
letters = lower + upper


def common_letter_score_for_triplet(x):
    first = set(list(x[0]))
    second = set(list(x[1]))
    third = set(list(x[2]))

    com = first.intersection(second)
    com2 = com.intersection(third)

    return letters.index(list(com2)[0]) + 1


bag_scores = [common_letter_score_for_triplet(bags[i:i + 3]) for i in range(0, len(bags), 3)]

print(sum(bag_scores))
