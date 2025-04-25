filename = './Day10/input.txt'
verbose = 0

f = open(filename, 'r')
new_lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

lines = []
for line in new_lines: # clean \n's
    this_line = list(map(int, line.rstrip()))
    lines.append([-1] + this_line + [-1])
    
# put -1 around edge
border = [-1] * len(lines[0])
lines.insert(0, border)
lines.append(border)

def find_trails(lines):
    trailheads = []
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if int(ch) == 0:
                trailheads.append([x,y])
    if verbose >= 5:
        print(f'Trailheads: {trailheads}')
    return trailheads

def traverse(trailhead_in, map_in, good_paths):
    # TODO: traverse through the map and count all places where 0 ascends smoothly to 9
    x = trailhead_in[0]
    y = trailhead_in[1]
    elev = map_in[y][x]
    
    if elev == 9:
        if verbose >= 3:
            print(f'Found a good exit at {trailhead_in}')
        good_paths.append(trailhead_in)
        return good_paths

    if verbose >= 5:
        print (f'Traversing up from {elev} at {[x,y]}')
    if map_in[y+1][x] == elev + 1:
        good_paths = traverse([x,y+1], map_in, good_paths)
    if map_in[y-1][x] == elev + 1:
        good_paths = traverse([x,y-1], map_in, good_paths)
    if map_in[y][x+1] == elev + 1:
        good_paths = traverse([x+1,y], map_in, good_paths)
    if map_in[y][x-1] == elev + 1:
        good_paths = traverse([x-1,y], map_in, good_paths)

    return good_paths

trailheads = find_trails(lines)
if verbose > 3:
    print(f'Number of trailheads found: {len(trailheads)}')

th_scores = []
for path_num, th in enumerate(trailheads):
    if verbose >= 3:
        print(f'\n- Starting trailhead number {path_num} -')
    good_paths = traverse(th, lines, [])
    unique_paths = []
    for path in good_paths:
        if path not in unique_paths:
            unique_paths.append(path)
    if verbose >= 3:
        print(f'Found {len(unique_paths)} unique paths.')
    th_scores.append(len(unique_paths))

if verbose > 3:
    print(f'Trailhead scores: {th_scores}')

print(f'\n Sum of all trailhead scores: {sum(th_scores)}')