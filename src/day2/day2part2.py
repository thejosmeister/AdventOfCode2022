# Day 2 part 2
# Once you start down the bad road it would be a waste of time to change it.
from common.common import parse_input_into_list_of_strings

scores_1 = {"rock": 1, "paper": 2, "scissors": 3}
scores_2 = {"l": 0, "d": 3, "w": 6}


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
        out.append("l")
    if parts[1] == "Y":
        out.append("d")
    if parts[1] == "Z":
        out.append("w")

    return out


def cal_win(x):
    if x[0] == x[1]:
        return 3

    if x[0] == "rock":
        if x[1] == "l":
            return scores_1["scissors"]
        if x[1] == "d":
            return scores_1["rock"] + scores_2[x[1]]
        if x[1] == "w":
            return scores_1["paper"] + scores_2[x[1]]

    if x[0] == "paper":
        if x[1] == "l":
            return scores_1["rock"]
        if x[1] == "d":
            return scores_1["paper"] + scores_2[x[1]]
        if x[1] == "w":
            return scores_1["scissors"] + scores_2[x[1]]

    if x[0] == "scissors":
        if x[1] == "l":
            return scores_1["paper"]
        if x[1] == "d":
            return scores_1["scissors"] + scores_2[x[1]]
        if x[1] == "w":
            return scores_1["rock"] + scores_2[x[1]]


input_list = parse_input_into_list_of_strings("input.txt")
pairs = [split_and_stuff(x) for x in input_list]
my_nums_2 = [cal_win(x) for x in pairs]

print(sum(my_nums_2))
