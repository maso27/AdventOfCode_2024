filename = './Day15/sample2.txt'
verbose = 5

# import numpy as np
if verbose >= 1:
    import time
    time_start = time.time()

def plot_map(map_list):
    for row in map_list:
        for ch in row:
            print(ch,end='')
        print('')

def widen_map(map_list):
    map_out = []
    for row in map_list:
        fat_row = ''
        for ch in row:
            if ch == '@':
                fat_row += '@.'
            elif ch == 'O':
                fat_row += '[]'
            else:
                fat_row += (ch + ch)
        map_out.append(list(fat_row))
    return map_out
            
def find_bot(map_in):
    for y, row in enumerate(map_in):
        for x, ch in enumerate(row):
            if ch == '@':
                return [x,y]
    print('No bot found')
    exit()

def find_boxes(map_in):
    coords = []
    for y, row in enumerate(map_in):
        for x, ch in enumerate(row):
            if ch == '[': # gps location is taken at left side of box
                coords.append([x,y])
    return coords

def push_boxes(map_a, directions):
    bot = find_bot(map_a)

    for rection in directions:
        if verbose >= 4:
            plot_map(map_a)
            print(f'Next direction: {rection}')

        if rection == '<':
            dir_go = [-1,0]
        elif rection == '^':
            dir_go = [0,-1]
        elif rection == '>':
            dir_go = [1,0]
        elif rection == 'v':
            dir_go = [0,1]
        else:
            print('Where are you going?')
            exit()

        next_loc = [bot[0] + dir_go[0], bot[1] + dir_go[1]]

        # step 1: look for wall
        if map_a[next_loc[1]][next_loc[0]] == '#':
            continue

        # step 2: nothing in the way
        if map_a[next_loc[1]][next_loc[0]] == '.':
            map_a[next_loc[1]][next_loc[0]] = '@'
            map_a[bot[1]][bot[0]] = '.'
            bot = next_loc
            continue

        # TODO: adjust step 3 for double-wide boxes
        # step 3: box in the way
        next_box = next_loc
        while map_a[next_box[1]][next_box[0]] == 'O': # skip past boxes in a line
            next_box = [next_box[0] + dir_go[0], next_box[1] + dir_go[1]]

        if map_a[next_box[1]][next_box[0]] == '#': # wall blocks boxes from moving
            continue

        map_a[next_box[1]][next_box[0]] = 'O'
        map_a[next_loc[1]][next_loc[0]] = '@'
        map_a[bot[1]][bot[0]] = '.'
        bot = next_loc
    return map_a

def sum_up(map_a):
    total = 0
    coords = find_boxes(map_a)
    for coord in coords:
        total += coord[0] + (coord[1] * 100)
    return total

f = open(filename, 'r')
new_lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

line = ''
map_a = []

# collect map
while line != '\n':
    line = new_lines.pop(0)
    map_a.append(list(line.rstrip()))

map_a = widen_map(map_a)

# collect directions
directions = ''
for line in new_lines:
    directions += line.rstrip()

if verbose >= 5:
    print('Initial Map:')
    plot_map(map_a)
    print('\nDirections:')
    print(directions)

map_a = push_boxes(map_a, directions)

if verbose >= 3:
    print('\nFinal Map:')
    plot_map(map_a)

total = sum_up(map_a)

print(f'Sum of final box coordinates: {total}')

if verbose >= 1:
    time_stop = time.time()
    print(f'\nTime passed: {time_stop-time_start}')
