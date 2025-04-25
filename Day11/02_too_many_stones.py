filename = './Day11/input.txt'
BLINKS = 40
VERBOSE = 1

import functools
if VERBOSE >= 1:
    import time
    time_start = time.time()

f = open(filename, 'r')
# new_lines = f.readlines() # reading all lines
line = f.readline()  # reading one line
f.close()

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

stones = line.split() # keep working with strings
# stones = list(map(int, line.split())) # ints

total_stones = 0

for one_stone in stones:
    if VERBOSE >= 3:
        print(f'\n - Running for stone {one_stone} -\n')
    these_stones = [one_stone]
    for a in range(BLINKS):
        stones_out = []
        for this_stone in these_stones:
            stones_temp = rules(this_stone)
            for temp in stones_temp:
                stones_out.append(temp)
        these_stones = stones_out
        if VERBOSE >= 5:
            print(f'After {a+1} blinks, the stone pattern is: {these_stones}')
    total_stones += len(these_stones)
    if VERBOSE >= 2:
        print(f'Time for this stone: {time.time()-time_start}')


print(f'Number of stones: {total_stones}')

if VERBOSE >= 1:
    time_stop = time.time()
    print(f'Time passed: {time_stop-time_start}')