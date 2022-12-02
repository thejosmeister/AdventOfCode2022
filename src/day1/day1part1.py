# Day 1 part 1
# Didn't mean to get up at 5
from common.common import parse_input_into_list_of_strings

input_list = parse_input_into_list_of_strings("input.txt")

elf_totals = []

current_tot = 0

for l in input_list:
    if l == "":
        elf_totals.append(current_tot)
        current_tot = 0
    else:
        current_tot += int(l)

elf_totals.append(current_tot)

print(max(elf_totals))
