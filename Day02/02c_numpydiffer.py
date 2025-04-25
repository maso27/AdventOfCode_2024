filename = './Day02/input.txt'
verbose = False

import numpy as np

f = open(filename, 'r')
lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

num_safe = 0

for line in lines:

    report = list(map(int, line.split())) # convert to integers

    # initial conditions
    is_safe = True
    increasing = False
    dampened = 0

    # establish increasing or decreasing
    updown = 0
    if (report[1] - report[0]) > 0:
        updown += 1
    if (report[2] - report[1]) > 0:
        updown += 1
    if (report[3] - report[2]) > 0:
        updown += 1
    if updown >= 2:
        increasing = True
    if verbose:
        if increasing:
            print(f'\nLine {report} is INCREASING')
        else:
            print(f'\nLine {report} is DECREASING')

    # diff based on increase or decrease
    a1 = np.array(report[1:], dtype=float)
    a2 = np.array(report[:-1], dtype=float)
    if increasing:
        diff_a = np.subtract(a1, a2)
    else:
        diff_a = np.subtract(a2, a1)
    
    if verbose:
        print(f' diff: {diff_a}')

    # check for too-big values
    temp_a = diff_a.copy()
    max_a = []
    while np.max(temp_a) > 3:
        idx = int(np.argmax(temp_a))
        max_a.append(idx)
        temp_a[idx] = 1.5 # put it in range
    # check for too-small values
    temp_a = diff_a.copy()
    min_a = []
    while np.min(temp_a) < 1:
        idx = int(np.argmin(temp_a))
        min_a.append(idx)
        temp_a[idx] = 1.5 # put it in range

    if verbose:
        print(f'  max_a: {max_a}, min_a: {min_a}')

    diff_sum = np.add(diff_a[1:], diff_a[:-1])
    if verbose:
        print(f'    diff_sum: {diff_sum}')

    outliers = max_a + min_a
    if 0 in outliers and 1 in outliers: # dumb hack
        dampened -= 1
    for idx in outliers:
        if idx >= 1: # not the first element
            prior_sum = diff_sum[idx-1]
        else:
            prior_sum = 1.5

        if idx < (len(diff_a) - 1): # not the last element
            next_sum = diff_sum[idx]
        else:
            next_sum = 1.5

        if verbose:
            print(f'   Index {idx}, prior_sum = {prior_sum}, next_sum = {next_sum}')
        if ((prior_sum >= 1 and prior_sum <= 3) or (next_sum >= 1 and next_sum <= 3)) and prior_sum != next_sum:
            print(f'Index {idx} is Dampenable')
            dampened += 1
        else:
            is_safe = False
            print(f'Index {idx} is NOT Dampenable')
    
    # temp_sum = diff_sum
    # dampened = 0
    # while np.max(temp_sum) > 6:
    #     idx = int(np.argmax(temp_sum))
    #     temp_sum = np.delete(temp_sum, idx)
    #     dampened += 1
    # while np.min(temp_sum) < 2:
    #     idx = int(np.argmin(temp_sum))
    #     temp_sum = np.delete(temp_sum, idx)
    #     dampened += 1
    
    if dampened < 2 and is_safe:
        num_safe += 1
        if verbose:
            print(f'Report {report} is SAFE')

print(f'Number of safe reports: {num_safe}')