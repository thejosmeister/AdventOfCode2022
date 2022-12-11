# Day 11 part 2
# Took me a while to remember what you can do with primes and modulo stuff
# First satisfying one in the advent of re-living my maths degree
from common.common import parse_input_into_list_of_strings
import re

rows = parse_input_into_list_of_strings("input.txt")

monkey_lists = [[] for i in range(8)]
monkey_ops = [lambda x: x * 3, lambda x: x + 7, lambda x: x + 5, lambda x: x + 8,lambda x: x + 4, lambda x: x * 2, lambda x: x + 6,lambda x: x * x]
monkey_tests = []
monkey_outs = [[] for t in range(8)]
monkey_checks = [0 for y in range(8)]

m_num = 0
for r in rows:
    if re.search('Monkey', r) is not None:
        m_num = int(re.search('Monkey (.):', r).group(1))
        continue
    if re.search('Starting items', r) is not None:
        parts = r.split(": ")
        for n in parts[1].split(', '):
            monkey_lists[m_num].append(int(n))
        continue
    if re.search('Test:', r) is not None:
        monkey_tests.append(int(re.search('Test: divisible by (.+)', r).group(1)))
        continue
    if re.search('If true: throw to monkey ', r) is not None:
        monkey_outs[m_num].append(int(re.search('If true: throw to monkey (.+)', r).group(1)))
        continue
    if re.search('If false: throw to monkey ', r) is not None:
        monkey_outs[m_num].append(int(re.search('If false: throw to monkey (.+)', r).group(1)))


r_round = 0
big_num = 1
for x in monkey_tests:  # going to do everything modulo the product of the primes
    big_num = big_num * x

for num in range(10000):
    for j in range(8):
        monkey_checks[j] += len(monkey_lists[j])
        for item in monkey_lists[j]:
            new_val = monkey_ops[j](item) % big_num
            if new_val % monkey_tests[j] == 0:
                monkey_lists[monkey_outs[j][0]].append(new_val)
            else:
                monkey_lists[monkey_outs[j][1]].append(new_val)

        monkey_lists[j] = []

a = sorted(monkey_checks)

print(a[-2] * a[-1])
