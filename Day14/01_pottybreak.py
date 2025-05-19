filename = './Day14/sample.txt'
verbose = 1

NUM_SECONDS = 100
ROOM_WIDTH = 11 # 101
ROOM_HEIGHT = 7 # 103

# import math
if verbose >= 1:
    import time
    time_start = time.time()

def parse_line(line_in):
    temp_dict = {}

    num_a = line_in.replace('=',' ').replace(',',' ').split()
    # should yield ['p',num,num,'v',num,num]
    temp_dict['start'] = [int(num_a[1]),int(num_a[2])]
    temp_dict['speed'] = [int(num_a[4]),int(num_a[5])]
    return temp_dict

def new_loc(bot):
    final_x = (bot['start'][0] + bot['speed'][0] * NUM_SECONDS) % ROOM_WIDTH
    final_y = (bot['start'][1] + bot['speed'][1] * NUM_SECONDS) % ROOM_HEIGHT
    return[final_x, final_y]


f = open(filename, 'r')
new_lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

bots_dict = {}

for this_bot,line in enumerate(new_lines):
    bots_dict[this_bot] = parse_line(line)
    bots_dict[this_bot]['end'] = new_loc(bots_dict[this_bot])

# TODO: separate into quadrants and count bots
# TODO: multiply quadrant results

if verbose >= 1:
    time_stop = time.time()
    print(f'\nTime passed: {time_stop-time_start}')