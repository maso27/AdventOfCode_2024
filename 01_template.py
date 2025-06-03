filename = './Day__/sample.txt'
verbose = 4

# import numpy as np
if verbose >= 1:
    import time
    time_start = time.time()

new_lines = []
with open (filename, 'r') as file:
    for line in file:
        new_lines.append(line.rstrip())
file.close()

if verbose >= 1:
    time_stop = time.time()
    print(f'\nTime passed: {time_stop-time_start}')