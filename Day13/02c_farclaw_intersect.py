filename = './Day13/input.txt'
verbose = 1

# import math
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

def find_combo(machine_in):
    a_x = machine_in['A']['X']
    b_x = machine_in['B']['X']
    a_y = machine_in['A']['Y']
    b_y = machine_in['B']['Y']
    end_x = machine_in['Prize']['X']
    end_y = machine_in['Prize']['Y']

    x = ((end_x/a_x) - (b_x*end_y)/(a_x*b_y)) / (1 - (b_x*a_y)/(a_x*b_y))
    y = (end_y / b_y) - (a_y*x / b_y)

    x = round(x,3)
    y = round(y,3)

    if x < 0 or y < 0 or x % 1 != 0 or y % 1 != 0: # negative or not integers
        if verbose >= 3:
            print(f'Intersection: {[x,y]}. Impossible to win machine {machine_in}')
        return []
    
    x = int(x)
    y = int(y)
    
    
    if verbose >= 5:
        print(f'Intersection: {[x,y]}')

    return [[x, y]]

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
        machines_dict[machine_num]['Prize']['X'] = int(this_line[1][2:-1]) + 10000000000000
        machines_dict[machine_num]['Prize']['Y'] = int(this_line[2][2:])   + 10000000000000

if verbose >= 3:
    for _,machine in machines_dict.items():
        print(machine)

costs = []

for _,machine in machines_dict.items():
    combos = find_combo(machine)
    costs.append(find_cost(combos))

if verbose >= 3:
    print(f'Costs of each machine: {costs}')

print(f'\nFinal cost to win all prizes: {sum(costs)} coins.')

if verbose >= 1:
    time_stop = time.time()
    print(f'\nTime passed: {time_stop-time_start}')