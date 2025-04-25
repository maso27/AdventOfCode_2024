filename = './Day03/input.txt'
verbose = True

# import numpy as np

do_do = True

def find_mul(line):
    global do_do
    locations = []
    mul_deep = 0
    do_deep = 0
    dont_deep = 0
    # do_do = True
    for idx, ch in enumerate(line):
        if do_deep == 0 and ch == 'd':
            do_deep += 1
        elif do_deep == 1:
            if ch == 'o':
                do_deep += 1
            else:
                do_deep = 0
        elif do_deep == 2:
            if ch == '(':
                do_deep += 1
            else:
                do_deep = 0
        elif do_deep == 3:
            if ch == ')':
                do_do = True
            do_deep = 0
        
        if dont_deep == 0 and ch == 'd':
            dont_deep += 1
        elif dont_deep == 1:
            if ch == 'o':
                dont_deep += 1
            else:
                dont_deep = 0
        elif dont_deep == 2:
            if ch == 'n':
                dont_deep += 1
            else:
                dont_deep = 0
        elif dont_deep == 3:
            if ch == "'":
                dont_deep += 1
            else:
                dont_deep = 0
        elif dont_deep == 4:
            if ch == "t":
                dont_deep += 1
            else:
                dont_deep = 0
        elif dont_deep == 5:
            if ch == "(":
                dont_deep += 1
            else:
                dont_deep = 0
        elif dont_deep == 6:
            if ch == ")":
                do_do = False
            dont_deep = 0
        
        if do_do:
            if mul_deep == 0 and ch == 'm':
                mul_deep += 1
            elif mul_deep == 1 and ch == 'u':
                mul_deep += 1
            elif mul_deep == 2 and ch == 'l':
                mul_deep = 0
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
        if mult1 > 999: # more than 3 digits
            continue
        if line[next_idx] != ',': # not valid
            continue
        next_idx += 1
        mult2 = 0
        while line[next_idx].isdigit():
            mult2 = (mult2 * 10) + int(line[next_idx]) 
            next_idx += 1
        if mult2 > 999: # more than 3 digits
            continue
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
    line_val = sum(num_list)
    full_sum += line_val
    
print(f'Full Sum: {full_sum}')
