filename = './Day15/sample3.txt'
verbose = 4

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

def mark_boxes(map_in):
    coords = []
    for y, row in enumerate(map_in):
        for x, ch in enumerate(row):
            if ch == '[': # gps location is taken at left side of box
                coords.append([x,y])
    return coords

def fill_box(map_in, coords):
    if map_in[coords[1]][coords[0]] == '[':
        return [coords,[coords[0]+1,coords[1]]]
    elif map_in[coords[1]][coords[0]] == ']':
        return [[coords[0]-1,coords[1]],coords]
    else:
        return [] # not a box
    
def push_map(map_a, box_coords, y):
    pushed_coords = []

    # place boxes in new locations
    # while box_coords:
    #     coord = box_coords.pop()
    for coord in reversed(box_coords): # gotta move the final ones first
        new_spot = [coord[0], coord[1] + y]
        pushed_coords.append(new_spot)
        map_a[new_spot[1]][new_spot[0]] = map_a[coord[1]][coord[0]] # move box to new spot

    # empty spaces in old locations
    for coord in box_coords:
        if coord not in pushed_coords:
            map_a[coord[1]][coord[0]] = '.'

    return map_a

def push_boxes(map_a, directions):
    bot = find_bot(map_a)

    for rection in directions:
        if verbose >= 4:
            plot_map(map_a)
            print(f'Next direction: {rection}')

        if rection == '<':
            x_go, y_go = -1,0
        elif rection == '^':
            x_go, y_go = 0,-1
        elif rection == '>':
            x_go, y_go = 1,0
        elif rection == 'v':
            x_go, y_go = 0,1
        else:
            print('Where are you going?')
            exit()

        next_loc = [bot[0] + x_go, bot[1] + y_go]

        # step 1: look for wall
        if map_a[next_loc[1]][next_loc[0]] == '#':
            continue

        # step 2: nothing in the way
        if map_a[next_loc[1]][next_loc[0]] == '.':
            map_a[next_loc[1]][next_loc[0]] = '@'
            map_a[bot[1]][bot[0]] = '.'
            bot = next_loc
            continue

        # step 3: box in the way
        next_box = next_loc

          # part 1: horizontal move
        if rection == '<' or rection == '>':
            while map_a[next_box[1]][next_box[0]] == '[' or map_a[next_box[1]][next_box[0]] == ']': # skip past boxes in a line
                next_box = [next_box[0] + 2*x_go, next_box[1] + 2*y_go]

            if map_a[next_box[1]][next_box[0]] == '#': # wall blocks boxes from moving
                continue

            # update box locations on map
            x = next_loc[0]
            if rection == '>':
                while x <= next_box[0]:
                    if map_a[next_loc[1]][x] == ']':
                        map_a[next_loc[1]][x] = '['
                    else:
                        map_a[next_loc[1]][x] = ']'
                    x += x_go
            else:
                while x >= next_box[0]:
                    if map_a[next_loc[1]][x] == '[':
                        map_a[next_loc[1]][x] = ']'
                    else:
                        map_a[next_loc[1]][x] = '['
                    x += x_go

          # part 2: vertical move
        else:
            no_wall = True
            check_boxes = fill_box(map_a, next_box)
            pushed_boxes = check_boxes.copy() # a list of all the boxes that need pushed
            while no_wall and check_boxes:
                check_boxes_temp = []
                for spot in check_boxes:
                    new_spot = [spot[0] + x_go, spot[1] + y_go]
                    if map_a[new_spot[1]][new_spot[0]] == '#':
                        no_wall = False
                        continue
                    if map_a[new_spot[1]][new_spot[0]] != '.':
                        check_boxes_temp += fill_box(map_a, new_spot)
                check_boxes = []
                [check_boxes.append(x) for x in check_boxes_temp if x not in check_boxes] # dropping duplicate coordinates
                pushed_boxes += check_boxes # used for actual box push
            if not no_wall: # hit a frickin' wall
                continue
            
            map_a = push_map(map_a, pushed_boxes, y_go)
          

        # handle bot and box move
        map_a[next_loc[1]][next_loc[0]] = '@'
        map_a[bot[1]][bot[0]] = '.'
        bot = next_loc
    return map_a

def sum_up(map_a):
    total = 0
    coords = mark_boxes(map_a)
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
