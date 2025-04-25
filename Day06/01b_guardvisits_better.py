filename = './Day06/input.txt'
verbose = True

dir_list = ['^','>','v','<'] # 0 through 3

def find_guard(lines):
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == '^' or ch == '>' or ch == '<' or ch == 'v':
                if verbose:
                    print(f'Found guard at {[x,y]}, facing {ch}')
                guard_dir = dir_list.index(ch)
                return [x,y], guard_dir
    print('WARNING: Guard not found!')
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

# def find_turns(block_locs, guard_loc, guard_dir):
#     turn_locs = []
#     if guard_dir == '^':
#         # do something here
#         pass
#     return block_locs

def find_path(block_locs, guard_loc, guard_dir, limits):
    path = []
    get_out = False
    
    while get_out == False:
        if guard_dir == 0: # ^
            check_loc = [guard_loc[0],guard_loc[1]-1]
        elif guard_dir == 1: # >
            check_loc = [guard_loc[0]+1,guard_loc[1]]
        elif guard_dir == 2: # v
            check_loc = [guard_loc[0],guard_loc[1]+1]
        elif guard_dir == 3: # <
            check_loc = [guard_loc[0]-1,guard_loc[1]]

        if check_loc in block_locs:
            guard_dir = (guard_dir + 1) % 4 # add 1 and wrap around
            if verbose:
                print(f'Guard found block at {check_loc}. Turning to {dir_list[guard_dir]}')
        elif check_loc[0] >= 0 and check_loc[0] <= limits[0] and check_loc[1] >= 0 and check_loc[1] <= limits[1]:
            guard_loc = check_loc
            if guard_loc not in path:
                path.append(guard_loc)
        else:
            get_out = True
    if verbose:
        print(f'Guard exited at {check_loc}')
    return path

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
    print(f'Establishing limits at {limits}')
guard_path = find_path(block_locs, guard_loc, guard_dir, limits)
print(f'Total number of locations for guard: {len(guard_path)}')