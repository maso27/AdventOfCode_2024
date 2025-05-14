filename = './Day13/input.txt'
verbose = 1

import math
if verbose >= 1:
    import time
    time_start = time.time()


A_COST = 3
B_COST = 1

def add_machine(machine_num):
    global machines_dict
    machines_dict[machine_num] = {}
    machines_dict[machine_num]['A'] = {}
    machines_dict[machine_num]['B'] = {}
    machines_dict[machine_num]['Prize'] = {}

def get_length(x_val, y_val):
    return math.sqrt(x_val^2 + y_val^2)

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
        if verbose >= 2:
            print(f'Impossible to win machine {machine_in}')
        return []

    a_first = get_length(a_xval, a_yval) > (3*get_length(b_xval, b_yval)) # A button more valuable than B button

    xval_1 = a_xval if a_first else b_xval
    yval_1 = a_yval if a_first else b_yval
    xval_2 = b_xval if a_first else a_xval
    yval_2 = b_yval if a_first else a_yval

    num_1 = 0
    while (xval_1 * num_1) <= total_xval:
        if verbose >= 5:
            print(num_1, end='\r')
        remaining_val = total_xval - (xval_1 * num_1)
        if remaining_val % xval_2 == 0:
            num_2 = int(remaining_val / xval_2)
            if (num_2 * yval_2) + (num_1 * yval_1) == total_yval:
                first_val = [num_1, num_2] if a_first else [num_2, num_1]
                if verbose >= 5:
                    print(f'Found match: {first_val}')
                return [first_val]
        num_1 += 1
    return []

def find_cost(combo_in):
    if not combo_in:
        return 0
    cost = (combo_in[0][0] * A_COST) + (combo_in[0][1] * B_COST)
    return cost

f = open(filename, 'r')
new_lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

machines_dict = {}
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
        machines_dict[machine_num]['Prize']['X'] = int(this_line[1][2:-1]) # + 10000000000000
        machines_dict[machine_num]['Prize']['Y'] = int(this_line[2][2:])   # + 10000000000000

if verbose >= 3:
    for _,machine in machines_dict.items():
        print(machine)

costs = []

for _,machine in machines_dict.items():
    combos = find_combos(machine)
    if verbose >= 3:
        print(f'Matching combos: {combos}')
    costs.append(find_cost(combos))

if verbose >= 3:
    print(f'Costs of each machine: {costs}')

print(f'Final cost to win all prizes: {sum(costs)} coins.')

if verbose >= 1:
    time_stop = time.time()
    print(f'\nTime passed: {time_stop-time_start}')