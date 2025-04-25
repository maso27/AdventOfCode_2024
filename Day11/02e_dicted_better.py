filename = './Day11/input.txt'
BLINKS = 75
VERBOSE = 1

if VERBOSE >= 1:
    import time
    time_start = time.time()

f = open(filename, 'r')
# new_lines = f.readlines() # reading all lines
line = f.readline()  # reading one line
f.close()

def store_stones(stones_in, qty):
    global stones_dict
    for stone in stones_in:
        if stone in stones_dict:
            stones_dict[stone]['num_stones'] += qty
        else:
            stones_dict[stone] = {}
            stones_dict[stone]['num_stones'] = qty
    return

def rules(stone_in, qty):
    if int(stone_in) == 0:
        store_stones(['1'], qty)
    elif len(stone_in) % 2 == 0:
        halfway = int(len(stone_in) / 2)
        first_half = str(int(stone_in[:halfway]))
        second_half = str(int(stone_in[halfway:]))
        store_stones([first_half, second_half], qty)
    else:
        store_stones([str(int(stone_in) * 2024)], qty)
    return

def count_stones():
    global stones_dict
    final_count = 0
    for stone_type in stones_dict:
        final_count += stones_dict[stone_type]['num_stones']
    return final_count

stones = line.split()

stones_dict = dict()

store_stones(stones, 1)

for a in range(BLINKS):

    working_dict = dict(stones_dict) # copy
    stones_dict.clear()
    for stone_type in working_dict:
        num_stones = working_dict[stone_type]['num_stones']
        rules(stone_type, num_stones)

    if VERBOSE >= 3:
        print(f'After {a+1} blinks, the stone makeup is: {stones_dict}')
        print(f'  Total stones: {count_stones()}')
    

time_stop = time.time()

print(f'Number of stones: {count_stones()}')

if VERBOSE >= 1:
    print(f'Time passed: {time_stop-time_start}')