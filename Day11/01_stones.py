filename = './Day11/input.txt'
BLINKS = 25
VERBOSE = 0

import functools
import time
time_start = time.time()

f = open(filename, 'r')
# new_lines = f.readlines() # reading all lines
line = f.readline()  # reading one line
f.close()

# line = list(map(int, line.rstrip()))

@functools.cache
def rules(stone_in):
    if int(stone_in) == 0:
        return ['1']
    elif len(stone_in) % 2 == 0:
        halfway = int(len(stone_in) / 2)
        first_half = str(int(stone_in[:halfway]))
        second_half = str(int(stone_in[halfway:]))
        return [first_half, second_half]
    else:
        return [str(int(stone_in) * 2024)]

stones = line.split()
for a in range(BLINKS):
    next_stones = []
    for stone in stones:
        stones_temp = rules(stone)
        for temp in stones_temp:
            next_stones.append(temp)
    if VERBOSE >= 3:
        print(f'After {a+1} blinks, the stone pattern is: {next_stones}')
    stones = next_stones

time_stop = time.time()

print(f'Number of stones: {len(stones)}')

print(f'Time passed: {time_stop-time_start}')