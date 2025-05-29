filename = './Day15/input.txt'
verbose = 1

import numpy as np
if verbose >= 1:
    import time
    time_start = time.time()

def plot_map(map_dict):
    walls_a = np.array(list(map_dict['walls']))
    boxes_a = np.array(list(map_dict['boxes']))
    width = walls_a[:,0].max() + 1 # furthest wall in x
    height = walls_a[:,1].max() + 1 # furthest wall in y
    map_list = [['.' for _ in range(width)] for _ in range(height)] # make blank map
    for loc in walls_a:
        map_list[loc[1]][loc[0]] = '#'
    for loc in boxes_a:
        map_list[loc[1]][loc[0]] = 'O'
    loc = map_dict['bot']
    map_list[loc[1]][loc[0]] = '@'

    for row in map_list:
        for ch in row:
            print(ch,end='')
        print('')

def parse_map(map_in):
    # TODO: double x coords
    boxes_out = []
    walls_out = []
    for y, row in enumerate(map_in):
        for x, ch in enumerate(row):
            if ch == '@':
                bot_out = [x,y]
            elif ch == 'O':
                boxes_out.append((x,y))
            elif ch == '#':
                walls_out.append((x,y))
    map_out = {}
    map_out['boxes'] = set(boxes_out)
    map_out['walls'] = set(walls_out)
    map_out['bot']   = np.array(bot_out)
    return map_out

def push_boxes(map_dict, directions):
    for rection in directions:
        if verbose >= 4:
            print(f'Direction: {rection}')

        if rection == '<':
            dir_go = np.array([-1,0])
        elif rection == '^':
            dir_go = np.array([0,-1])
        elif rection == '>':
            dir_go = np.array([1,0])
        elif rection == 'v':
            dir_go = np.array([0,1])
        else: 
            print('Where are you going?')
            exit()

        next_loc = map_dict['bot'] + dir_go
        # step 1: look for wall
        if tuple(next_loc) in map_dict['walls']:
            # print(f'found wall at {next_loc}')
            continue

        # step 2: look for open space
        if tuple(next_loc) not in map_dict['boxes']:
            # print(f'Open space at {next_loc}')
            map_dict['bot'] = next_loc
            continue

        # step 3: move boxes
        # TODO: handle double-wide boxes
        next_box = next_loc.copy()
        while tuple(next_box) in map_dict['boxes']:
            # print(f'Pushing box at {next_box}')
            next_box += dir_go
        
        if tuple(next_box) in map_dict['walls']:
            # print(f'Box hits wall at {next_box}')
            continue

        map_dict['bot'] = next_loc.copy()
        map_dict['boxes'].discard(tuple(next_loc))
        map_dict['boxes'].add(tuple(next_box))
                                     
    return map_dict

def sum_up(map_in):
    total = 0
    for box in map_in['boxes']:
        total += box[0] + (box[1] * 100)
    return total

f = open(filename, 'r')
new_lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

line = ''
map_l = []

# collect map
while line != '\n':
    line = new_lines.pop(0)
    map_l.append(line.rstrip())

# collect directions
directions = ''
for line in new_lines:
    directions += line.rstrip()

# strip map to coordinates
map_dict = parse_map(map_l)

if verbose >= 4:
    print('Starting map:')
    plot_map(map_dict)

if verbose >= 5:
    print('\nDirections:')
    print(directions)


map_dict = push_boxes(map_dict, directions)
if verbose >= 2:
    print('Final map:')
    plot_map(map_dict)

final_sum = sum_up(map_dict)

print(f'Sum of final box coordinates: {final_sum}')

if verbose >= 1:
    time_stop = time.time()
    print(f'\nTime passed: {time_stop-time_start}')