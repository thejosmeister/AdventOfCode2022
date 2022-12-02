# Day 2 part 1
# Not the nicest soln but I feel this one was a bit parse heavy.
from common.common import parse_input_into_list_of_strings

scores_1 = {"rock": 1, "paper": 2, "scissors": 3}


def split_and_stuff(x):
    parts = x.split()

    out = []

    if parts[0] == "A":
        out.append("rock")
    if parts[0] == "B":
        out.append("paper")
    if parts[0] == "C":
        out.append("scissors")

    if parts[1] == "X":
        out.append("rock")
    if parts[1] == "Y":
        out.append("paper")
    if parts[1] == "Z":
        out.append("scissors")

    return out


def cal_win(x):
    if x[0] == x[1]:
        return 3

    if x[0] == "rock":
        if x[1] == "paper":
            return 6
        if x[1] == "scissors":
            return 0

    if x[0] == "paper":
        if x[1] == "scissors":
            return 6
        if x[1] == "rock":
            return 0

    if x[0] == "scissors":
        if x[1] == "rock":
            return 6
        if x[1] == "paper":
            return 0


input_list = parse_input_into_list_of_strings("input.txt")
pairs = [split_and_stuff(x) for x in input_list]
my_nums = [scores_1[x[1]] for x in pairs]
my_nums_2 = [cal_win(x) for x in pairs]
r = []
for i1, i2 in zip(my_nums, my_nums_2):
    r.append(i1 + i2)

print(sum(r))
