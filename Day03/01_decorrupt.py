filename = './Day03/input.txt'
verbose = True

# import numpy as np

def find_mul(line):
    locations = []
    ch_deep = 0
    for idx, ch in enumerate(line):
        if ch_deep == 0 and ch == 'm':
            ch_deep += 1
        elif ch_deep == 1 and ch == 'u':
            ch_deep += 1
        elif ch_deep == 2 and ch == 'l':
            ch_deep = 0
            locations.append(idx + 1)
    # return locations
    multiplicands = []
    for idx in locations:
        if line[idx] != '(': # not valid
            continue 
        next_idx = idx + 1
        mult1 = 0
        while line[next_idx].isdigit():
            mult1 = (mult1 * 10) + int(line[next_idx])
            next_idx += 1
        if line[next_idx] != ',': # not valid
            continue
        next_idx += 1
        mult2 = 0
        while line[next_idx].isdigit():
            mult2 = (mult2 * 10) + int(line[next_idx]) 
            next_idx += 1
        if line[next_idx] != ')': # not valid
            continue
        multiplicands.append(mult1 * mult2)
    return multiplicands
    
f = open(filename, 'r')
lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

full_sum = 0
for line in lines:
    # find "mul(x,y)" structure
    num_list = find_mul(line)
    if verbose:
        print(num_list)
    line_val = sum(find_mul(line))
    full_sum += line_val
    
print(f'Full Sum: {full_sum}')
