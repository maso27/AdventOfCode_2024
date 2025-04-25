filename = './Day04/input.txt'
verbose = False

f = open(filename, 'r')
lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

def find_first(lines, char_in = 'X'):
    firsts = []
    for y_val, line in enumerate(lines):
        for x_val, ch in enumerate(line):
            if ch.upper() == char_in:
                firsts.append([y_val,x_val])
                if verbose:
                    print(f'Found {char_in} at ({x_val},{y_val})')
    return firsts

def find_second(lines, arr_in, char_in = 'M'):
    seconds = [] # contains x coords, then resulting m coords
    for coords in arr_in:
        x_vals = []
        y_vals = []
        if coords[0] > 0: # not first line
            y_vals.append(coords[0]-1)
        y_vals.append(coords[0])
        if coords[0] < len(lines)-2: # not last line
            y_vals.append(coords[0]+1)

        if coords[1] > 0: # not first character
            x_vals.append(coords[1]-1)
        x_vals.append(coords[1])
        if coords[1] < len(lines[0])-2: # not last character
            x_vals.append(coords[1]+1)

        for y in y_vals:
            for x in x_vals:
                if lines[y][x].upper() == char_in:
                    seconds.append([coords, [y,x]])
                    if verbose:
                        print(f'X at {coords}, M at {[y,x]}')
    return seconds

def find_next(lines, arr_in, char_in):
    nexts = []
    for coords in arr_in:
        last = coords[-1]
        prev = coords[-2]
        next_y = last[0] + (last[0]-prev[0])
        next_x = last[1] + (last[1]-prev[1])
        if (next_y < 0) or (next_y > len(lines)-1) or (next_x < 0) or (next_x > len(lines[0])-1):
            continue
        if lines[next_y][next_x] == char_in:
            nexts.append(coords + [[next_y,next_x]])
            if verbose:
                print(f'{coords} -- {char_in} at {[next_y, next_x]}')
    return nexts

exes = find_first(lines,        'X')
emms = find_second(lines, exes, 'M')
ayys = find_next(lines,   emms, 'A')
esss = find_next(lines,   ayys, 'S')

print(f'XMAS occurs {len(esss)} times.')