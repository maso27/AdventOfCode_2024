filename = './Day11/input.txt'
BLINKS = 25
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

def recurse(stone_in, num_blinks):
    global num_stones
    if num_blinks >= BLINKS:
        if VERBOSE >= 5:
            print(f'All blinks on stone {stone_in}')
        num_stones += 1
        return
    
    num_blinks += 1
    stones_back = rules(stone_in)
    for stone in stones_back:
        recurse(stone, num_blinks)
    if VERBOSE >= 5:
        print(f'Number of stones returning: {num_stones}')
    return

stones = line.split() # keep working with strings
# stones = list(map(int, line.split())) # ints

num_stones = 0

for one_stone in stones:
    if VERBOSE >= 3:
        print(f'\n - Running for stone {one_stone} -\n')

    recurse(one_stone, 0)
    
    if VERBOSE >= 4:
        print(f'Number of stones: {num_stones}')
    if VERBOSE >= 2:
        print(f'Time for this stone: {time.time()-time_start}')


print(f'Number of stones: {num_stones}')

if VERBOSE >= 1:
    time_stop = time.time()
    print(f'Time passed: {time_stop-time_start}')