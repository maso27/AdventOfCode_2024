filename = './Day13/sample.txt'
verbose = 1

import math
if verbose >= 1:
    import time
    time_start = time.time()


A_COST = 3
B_COST = 1

def add_machine(machine_num):
    global machines_dict
    machines_dict[machine_num] = dict()
    machines_dict[machine_num]['A'] = dict()
    machines_dict[machine_num]['B'] = dict()
    machines_dict[machine_num]['Prize'] = dict()

def find_combos(machine_in):
    a_xval = machine_in['A']['X']
    b_xval = machine_in['B']['X']
    a_yval = machine_in['A']['Y']
    b_yval = machine_in['B']['Y']
    total_xval = machine_in['Prize']['X']
    total_yval = machine_in['Prize']['Y']

    common_d_x = math.gcd(a_xval, b_xval)
    common_d_y = math.gcd(a_yval, b_yval)

    if (total_xval % common_d_x != 0) or (total_yval % common_d_y != 0): # it is impossible
        if verbose >= 5:
            print(f'Impossible to win machine {machine_in}')
        return []
    
    # find first solution
    a_num = 0
    while (a_xval * a_num) <= total_xval:
        remaining_val = total_xval - (a_xval * a_num)
        if remaining_val % b_xval == 0:
            b_num = int(remaining_val / b_xval)
            first_combo = [a_num, b_num]
            if verbose >= 5:
                print(f'First combo found: {first_combo}')
            # return [first_combo]
            break
        a_num += 1

    # # find first solution, backwards
    # b_num = 0
    # while (b_xval * b_num) <= total_xval: # just to keep from infinite loop
    #     remaining_val = total_xval - (b_xval * b_num)
    #     if remaining_val % a_xval == 0:
    #         a_num = int(remaining_val / a_xval)
    #         first_combo = [a_num, b_num]
    #         if verbose >= 5:
    #             print(f'First combo found: {first_combo} (backwards)')
    #         # return [first_combo]
    #         break
    #     b_num += 1

    iterator = int(b_xval/common_d_x)
    combos = []
    a = 0
    while (a_xval * a_num) <= total_xval:
        a_num = first_combo[0] + a*iterator
        remaining_val = total_xval - (a_xval * a_num)
        if remaining_val % b_xval == 0:
            b_num = int(remaining_val / b_xval)
            if (a_num * a_yval) + (b_num * b_yval) == total_yval:
                combos.append([a_num, b_num])
                if verbose >= 5:
                    print(f'Adding new combo: {[a_num, b_num]}')
        a += 1
    return combos

def find_cheapest(combos_in):
    if not combos_in:
        return 0
    costs = []
    for combo in combos_in:
        costs.append((combo[0] * A_COST) + (combo[1] * B_COST))
        if verbose >= 5:
            print(f'combo {combo} will cost {(combo[0] * A_COST) + (combo[1] * B_COST)}')
    costs.sort()
    if verbose >= 4:
        print(f'Sorted costs: {costs}')
    return costs[0]

f = open(filename, 'r')
new_lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

machines_dict = dict()
machine_num = 0
add_machine(machine_num)

for line in new_lines:
    this_line = line.split()
    if not this_line: # empty line
        machine_num += 1
        add_machine(machine_num)
    elif this_line[0] == 'Button':
        this_button = this_line[1][0]
        machines_dict[machine_num][this_button]['X'] = int(this_line[2][2:-1])
        machines_dict[machine_num][this_button]['Y'] = int(this_line[3][2:])
    elif this_line[0] == 'Prize:':
        machines_dict[machine_num]['Prize']['X'] = int(this_line[1][2:-1]) + 10000000000000
        machines_dict[machine_num]['Prize']['Y'] = int(this_line[2][2:])   + 10000000000000

if verbose >= 3:
    for machine in machines_dict:
        print(machines_dict[machine])

costs = []

for machine in machines_dict:
    this_machine = machines_dict[machine]
    combos = find_combos(this_machine)
    if verbose >= 3:
        print(f'Matching combos: {combos}')
    costs.append(find_cheapest(combos))

if verbose >= 3:
    print(f'Costs of each machine: {costs}')

print(f'Final cost to win all prizes: {sum(costs)} coins.')

if verbose >= 1:
    time_stop = time.time()
    print(f'\nTime passed: {time_stop-time_start}')