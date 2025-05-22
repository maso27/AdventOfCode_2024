filename = './Day15/sample.txt'
verbose = 5

import numpy as np
if verbose >= 1:
    import time
    time_start = time.time()

def plot_map(map_dict):
    width = map_dict['walls'][:,0].max() + 1 # furthest wall in x
    height = map_dict['walls'][:,1].max() + 1 # furthest wall in y
    map_list = [['.' for _ in range(width)] for _ in range(height)] # make blank map
    for loc in map_dict['walls']:
        map_list[loc[1]][loc[0]] = '#'
    for loc in map_dict['boxes']:
        map_list[loc[1]][loc[0]] = 'O'
    loc = map_dict['bot']
    map_list[loc[1]][loc[0]] = '@'

    for row in map_list:
        for ch in row:
            print(ch,end='')
        print('')

def parse_map(map_in):
    boxes_out = []
    walls_out = []
    for y, row in enumerate(map_in):
        for x, ch in enumerate(row):
            if ch == '@':
                bot_out = [x,y]
            elif ch == 'O':
                boxes_out.append([x,y])
            elif ch == '#':
                walls_out.append([x,y])
    map_dict = {}
    map_dict['boxes'] = np.array(boxes_out)
    map_dict['walls'] = np.array(walls_out)
    map_dict['bot']   = np.array(bot_out)
    return map_dict

def push_boxes(map, directions):
    for rection in directions:
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
        # TODO: figure out how to recursively push stuff


f = open(filename, 'r')
new_lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

line = ''
map = []

# collect map
while line != '\n':
    line = new_lines.pop(0)
    map.append(line.rstrip())

# collect directions
directions = ''
for line in new_lines:
    directions += line.rstrip()

# strip map to coordinates
map_dict = parse_map(map)

if verbose >= 4:
    print('Starting map:')
    plot_map(map_dict)
    # print(f'Bot is at {map_dict['bot']}')

if verbose >= 5:
    print('\nDirections:')
    print(directions)



# TODO: figure out how to push boxes
# TODO: sum coordinates

if verbose >= 1:
    time_stop = time.time()
    print(f'\nTime passed: {time_stop-time_start}')