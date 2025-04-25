filename = './Day07/input.txt'
verbose = 4

f = open(filename, 'r')
new_lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

lines = []
for line in new_lines: # clean \n's
    lines.append(line.rstrip())

def run_the_numbers(result, vars):
    last_combos = [vars.pop(0)]
    for var in vars:
        next_combos = []
        for combo in last_combos:
            next_combos.append(combo * var)
            next_combos.append(combo + var)

            # concatenation
            var_temp = var # float(var)
            combo_temp = combo
            while var_temp >= 1:
                combo_temp *= 10
                var_temp /= 10
            cat_num = combo_temp + var
            cat_str = int(str(combo)+str(var))
            if verbose >= 4:
                if cat_num != cat_str:
                    print(f'Error!  Result {result} has a failure!')
                    print(f'Cat_num: {cat_num}\tCat_str: {cat_str}')
                    print(f'Variables: {vars}')
            next_combos.append(cat_num)
            # next_combos.append(int(str(combo)+str(var)))
        last_combos = next_combos.copy()
    if verbose == 5:
        print(f'All combinations: {next_combos}')
    if result in next_combos:
        return True
    return False

passing_values = []
for line in lines:
    split_line = line.split(':') # remove the result
    result = int(split_line[0])
    split_line = split_line[1].split() # separate the rest
    vars = list(map(int, split_line)) # convert to integers
    if verbose == 5:
        print(f'Line: {line}')
        print(f' Result: {result}\tVariables: {vars}')
    order = []
    for a in range(len(vars)-1):
        order.append(0)
    is_valid = run_the_numbers(result, vars)
    if is_valid:
        if verbose == 5:
            print(f'{result} is valid')
        passing_values.append(result)

if verbose >= 2:
    print(f'\nPassing values: {passing_values}')
print(f'\n - Final Sum: {sum(passing_values)} -')

# 40653385348798 was too low