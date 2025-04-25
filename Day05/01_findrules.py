filename1 = './Day05/input_rules.txt'
filename2 = './Day05/input_updates.txt'
verbose = False

import numpy as np

f = open(filename1, 'r')
rules = f.readlines()
f.close()

f = open(filename2, 'r')
updates = f.readlines()
f.close()

# build update tables
rules_list = []
first_rule = []
second_rule = []
for rule in rules:
    rule = list(map(int, rule.split('|')))
    rules_list.append(rule)
    first_rule.append(rule[0])
    second_rule.append(rule[1])
rules_a = np.array(rules_list)

passing_lines  = []
middle_numbers = []
for update_idx, update in enumerate(updates):
    update = np.array(list(map(int, update.split(','))))
    # if verbose:
    #     print(f'Testing line: {update}')
    failed = False
    for rule in rules_a:
        first_idx = np.where(update == rule[0])[0]
        if np.size(first_idx) > 0: # if first_idx is not None:
            second_idx = np.where(update == rule[1])[0]
            if np.size(second_idx) > 0: # if second_idx is not None:
                if first_idx[0] > second_idx[0]:
                    failed = True
                    if verbose:
                        print(f'{update_idx}: FAILED, {update}, {rule[0]} | {rule[1]}')
    if failed == False:
        if verbose:
            print(f'{update_idx}: PASSED, {update}')
        passing_lines.append(update_idx)
        mid_idx = int(len(update) / 2)
        middle_numbers.append(update[mid_idx])

if verbose:
    print(f'Passing lines:  {passing_lines}')
    print(f'Middle numbers: {middle_numbers}')


print(f'Sum of all passing middle numbers: {sum(middle_numbers)}')