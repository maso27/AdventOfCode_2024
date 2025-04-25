filename = './Day06/input.txt'
verbose = False

def find_guard(lines):
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == '^' or ch == '>' or ch == '<' or ch == 'v':
                return [x,y], ch
    return [-1,-1], 'x'

f = open(filename, 'r')
lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

guard_path = []
guard_loc, guard_dir = find_guard(lines)
if verbose:
    print(f'Found guard at {guard_loc}, facing {guard_dir}')
guard_path.append(guard_loc)

while (guard_loc[0] >= 0 and guard_loc[0] < len(lines[0])) and (guard_loc[1] >= 0 and guard_loc[1] < len(lines)):
    new_dir = guard_dir
    if guard_dir == '^':
        new_loc = [guard_loc[0], guard_loc[1]-1]
        if lines[new_loc[1]][new_loc[0]] == '#':
            new_dir = '>'
            new_loc = guard_loc
    elif guard_dir == '>':
        new_loc = [guard_loc[0]+1, guard_loc[1]]
        if lines[new_loc[1]][new_loc[0]] == '#':
            new_dir = 'v'
            new_loc = guard_loc
    elif guard_dir == 'v':
        new_loc = [guard_loc[0], guard_loc[1]+1]
        if lines[new_loc[1]][new_loc[0]] == '#':
            new_dir = '<'
            new_loc = guard_loc
    elif guard_dir == '<':
        new_loc = [guard_loc[0]-1, guard_loc[1]]
        if lines[new_loc[1]][new_loc[0]] == '#':
            new_dir = '^'
            new_loc = guard_loc
    guard_dir = new_dir
    guard_loc = new_loc
    if guard_loc not in guard_path:
        guard_path.append(guard_loc)

guard_path.pop() # last step was out-of-bounds
if verbose:
    print(f'Guard Path: {guard_path}')
print(f'Guard unique locations: {len(guard_path)}')