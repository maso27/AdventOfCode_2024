filename = './Day14/input.txt'
verbose = 1

NUM_SECONDS = 100
ROOM_WIDTH =  101 # 11
ROOM_HEIGHT = 103 # 7

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

def new_loc(bot_in):
    temp_dict = {}
    temp_dict['X'] = (bot_in['start']['X'] + bot_in['speed']['X'] * NUM_SECONDS) % ROOM_WIDTH
    temp_dict['Y'] = (bot_in['start']['Y'] + bot_in['speed']['Y'] * NUM_SECONDS) % ROOM_HEIGHT
    return temp_dict

def split_quads(bots_in):
    mid_x = int(ROOM_WIDTH / 2)
    mid_y = int(ROOM_HEIGHT / 2)
    nw = []
    ne = []
    sw = []
    se = []
    for _,bot in bots_in.items():
        if bot['end']['X'] < mid_x and bot['end']['Y'] < mid_y:
            nw.append([bot['end']['X'],bot['end']['Y']])
        elif bot['end']['X'] > mid_x and bot['end']['Y'] < mid_y:
            ne.append([bot['end']['X'],bot['end']['Y']])
        elif bot['end']['X'] < mid_x and bot['end']['Y'] > mid_y:
            sw.append([bot['end']['X'],bot['end']['Y']])
        elif bot['end']['X'] > mid_x and bot['end']['Y'] > mid_y:
            se.append([bot['end']['X'],bot['end']['Y']])
    return nw, ne, sw, se


f = open(filename, 'r')
new_lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

bots_dict = {}

for this_bot,line in enumerate(new_lines):
    bots_dict[this_bot] = parse_line(line)
    bots_dict[this_bot]['end'] = new_loc(bots_dict[this_bot])

if verbose >= 5:
    print('\nStart Points:')
    for _,bot in bots_dict.items():
        print(f" ({bot['start']}")
if verbose >= 3:
    print('\nEnd Points:')
    for _,bot in bots_dict.items():
        print(f" ({bot['end']}")

nw, ne, sw, se = split_quads(bots_dict)

if verbose >= 2:
    print('\nNW Quad:')
    for point in nw:
        print(point)
    print('NE Quad:')
    for point in ne:
        print(point)
    print('SW Quad:')
    for point in sw:
        print(point)
    print('SE quad:')
    for point in se:
        print(point)

safety_factor = len(nw) * len(ne) * len(sw) * len(se)

print(f'\n SAFETY FACTOR: {safety_factor}')

if verbose >= 1:
    time_stop = time.time()
    print(f'\nTime passed: {time_stop-time_start}')
