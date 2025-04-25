import time
time_start = time.time()

filename = './Day06/input.txt'
verbose = True

dir_list = ['^','>','v','<'] # 0 through 3

def find_guard(lines):
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == '^' or ch == '>' or ch == '<' or ch == 'v':
                # if verbose:
                #     print(f'\n - Found guard at {[x,y]}, facing {ch} -\n')
                guard_dir = dir_list.index(ch)
                return [x,y], guard_dir
    print('\n - WARNING: Guard not found! -\n')
    return [-1,-1], -1

def find_blocks(lines):
    block_locs = []
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == '#':
                block_locs.append([x,y])
                if verbose:
                    print(f'Block found at {[x,y]}')
    return block_locs

def find_path(block_locs, guard_loc, guard_dir, limits):
    path = []
    get_out = False
    
    seen_blocks = []
    is_loop = False

    while get_out == False:
        if guard_dir == 0: # ^
            check_loc = [guard_loc[0],guard_loc[1]-1]
        elif guard_dir == 1: # >
            check_loc = [guard_loc[0]+1,guard_loc[1]]
        elif guard_dir == 2: # v
            check_loc = [guard_loc[0],guard_loc[1]+1]
        elif guard_dir == 3: # <
            check_loc = [guard_loc[0]-1,guard_loc[1]]

        # if [check_loc, guard_dir] in seen_blocks: 
        #     if verbose:
        #         print(f'\nGuard already saw {check_loc} facing {dir_list[guard_dir]}, STUCK IN LOOP! -\n')
        #     is_loop = True
        #     get_out = True

        if check_loc in block_locs:
            guard_dir = (guard_dir + 1) % 4 # add 1 and wrap around
            if [check_loc, guard_dir] in seen_blocks: 
                if verbose:
                    print(f'\nGuard already saw {check_loc} facing {dir_list[guard_dir]}, STUCK IN LOOP! -\n')
                is_loop = True
                get_out = True
            seen_blocks.append([check_loc, guard_dir])
            # if verbose:
            #     print(f'Guard found block at {check_loc}. Turning to {dir_list[guard_dir]}')
        elif check_loc[0] >= 0 and check_loc[0] <= limits[0] and check_loc[1] >= 0 and check_loc[1] <= limits[1]:
            guard_loc = check_loc
            if guard_loc not in path:
                path.append(guard_loc)
        else:
            get_out = True
    # if verbose:
    #     print(f'\n - Guard exited at {check_loc} -\n')
    return path, is_loop

f = open(filename, 'r')
new_lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

lines = []
for line in new_lines: # clean \n's
    lines.append(line.rstrip())

guard_loc, guard_dir = find_guard(lines)

block_locs = find_blocks(lines) 
# guard_turns = find_turns(block_locs, guard_loc, guard_dir)
limits = [len(lines[-1])-1, len(lines)-1]
if verbose:
    print(f'\n - Establishing limits at {limits} - \n')
guard_path, loop = find_path(block_locs, guard_loc, guard_dir, limits)
print(f'Total number of locations for guard: {len(guard_path)}')

num_loops = 0
loop_locs = []
if guard_loc in guard_path:
    if verbose:
        print("Found guard_loc in path, can't place block there.")
    guard_path.remove(guard_loc)
for newblock_loc in guard_path:
    # guard_loc, guard_dir = find_guard(lines) # re-initalize guard
    addblock_locs = block_locs.copy()
    addblock_locs.append(newblock_loc)
    if verbose:
        print(f" - Adding block at {newblock_loc} -")
    _, loop = find_path(addblock_locs, guard_loc, guard_dir, limits)
    if loop:
        num_loops += 1
        loop_locs.append(newblock_loc)

time_stop = time.time()
print(f'Loop Locations: {loop_locs}')
print(f'Number of possible loops: {num_loops}')
print(f'Time passed: {time_stop-time_start}')