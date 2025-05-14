filename = './Day13/sample.txt'
verbose = 1

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

def find_x_combos(a_val, b_val, total_val):
    combos = []
    a_num = 0
    while (a_val * a_num) <= total_val:
        remaining_val = total_val - (a_val * a_num)
        if remaining_val % b_val == 0:
            b_num = int(remaining_val / b_val)
            combos.append([a_num, b_num])
        a_num += 1
    return combos

def check_y_combos(a_val, b_val, total_val, combos_in):
    combos_out = []
    for combo in combos_in:
        if (combo[0] * a_val) + (combo[1] * b_val) == total_val:
            combos_out.append(combo)
    return combos_out

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
        machines_dict[machine_num]['Prize']['X'] = int(this_line[1][2:-1])
        machines_dict[machine_num]['Prize']['Y'] = int(this_line[2][2:])

if verbose >= 5:
    for _,machine in machines_dict.items():
        print(machine)

costs = []

for _, machine in machines_dict.items():
    combos_x =        find_x_combos(machine['A']['X'], machine['B']['X'], machine['Prize']['X'])
    combos_matched = check_y_combos(machine['A']['Y'], machine['B']['Y'], machine['Prize']['Y'], combos_x)
    if verbose >= 3:
        print(f'Possible X combos: {combos_x}')
        print(f'Matching Y combos: {combos_matched}')
    costs.append(find_cheapest(combos_matched))

if verbose >= 3:
    print(f'Costs of each machine: {costs}')

print(f'Final cost to win all prizes: {sum(costs)} coins.')

if verbose >= 1:
    time_stop = time.time()
    print(f'\nTime passed: {time_stop-time_start}')