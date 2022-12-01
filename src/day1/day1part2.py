# Day 1 part 2
from common.common import parse_input_into_list_of_strings

list = parse_input_into_list_of_strings("input.txt")

elf_totals = []

current_tot = 0

for l in list:
    if l == "":
        elf_totals.append(current_tot)
        current_tot = 0
    else:
        current_tot += int(l)

elf_totals.append(current_tot)

elf_totals = sorted(elf_totals)

print(sum(elf_totals[-3:]))
