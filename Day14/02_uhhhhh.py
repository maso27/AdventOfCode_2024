filename = './Day14/input.txt'
verbose = 1

NUM_SECONDS = 100
ROOM_WIDTH =  101 # 11
ROOM_HEIGHT = 103 # 7
DUPES_THRESH = 1

if verbose >= 1:
    import time
    time_start = time.time()

def parse_line(line_in):
    temp_dict = {}

    num_a = line_in.replace('=',' ').replace(',',' ').split()
    # should yield ['p',num,num,'v',num,num]
    temp_dict['start'] = {}
    temp_dict['speed'] = {}
    temp_dict['start']['X'] = int(num_a[1])
    temp_dict['start']['Y'] = int(num_a[2])
    temp_dict['speed']['X'] = int(num_a[4])
    temp_dict['speed']['Y'] = int(num_a[5])
    return temp_dict

def new_loc(bot_in, num_seconds = NUM_SECONDS):
    x_loc = (bot_in['start']['X'] + bot_in['speed']['X'] * num_seconds) % ROOM_WIDTH
    y_loc = (bot_in['start']['Y'] + bot_in['speed']['Y'] * num_seconds) % ROOM_HEIGHT
    return [x_loc, y_loc]

def check_spread(end_list):
# return number of bots that are on top of each other
    dupes = 0
    while end_list:
        coords = end_list.pop()
        if coords in end_list:
            dupes += 1
    return dupes

def display_bots(end_list):
# visualize the map
    bot_map = []
    for a in range(ROOM_HEIGHT):
        bot_map.append(['.'] * ROOM_WIDTH)
    for bot_loc in end_list:
        bot_map[bot_loc[1]][bot_loc[0]] = 'X'

    print('\n LATEST MAP:')
    for row in bot_map:
        for char in row:
            print(char,end='')
        print('')

f = open(filename, 'r')
new_lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

bots_dict = {}

for this_bot,line in enumerate(new_lines):
    bots_dict[this_bot] = parse_line(line)

num_sec = 0
latest_locs = []
exit_flag = False

while exit_flag == False:
    for _,bot in bots_dict.items():
        latest_locs.append(new_loc(bot, num_sec))
    num_dupes = check_spread(latest_locs.copy())

    if num_dupes < DUPES_THRESH:
        display_bots(latest_locs)
        print(f'Iteration: {num_sec}\tDupes: {num_dupes}')
        yesno = input('Continue? (y/n): ')
        if yesno.lower() != 'y':
            exit_flag = True

    latest_locs = []
    num_sec += 1

print(f'\nFinal Iteration: {num_sec-1}\tDupes: {num_dupes}')

if verbose >= 1:
    time_stop = time.time()
    print(f'\nTime passed: {time_stop-time_start}')