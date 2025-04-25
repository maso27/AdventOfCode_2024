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

def find_cross(lines, arr_in):
    crosses = []
    for coords in arr_in:
        if (coords[0] <= 0) or (coords[1] <= 0) or (coords[0] >= len(lines)-1) or (coords[1] >= len(lines[0])-1):
            continue
        nw_char = lines[coords[0]-1][coords[1]-1].upper()
        ne_char = lines[coords[0]-1][coords[1]+1].upper()
        sw_char = lines[coords[0]+1][coords[1]-1].upper()
        se_char = lines[coords[0]+1][coords[1]+1].upper()
        if (nw_char == 'M' and se_char == 'S') or (nw_char == 'S' and se_char == 'M'):
            if (ne_char == 'M' and sw_char == 'S') or (ne_char == 'S' and sw_char == 'M'):
                crosses.append(coords)
    return crosses



ayys    = find_first(lines,  'A')
crosses = find_cross(lines,   ayys)

print(f'cross-MAS occurs {len(crosses)} times.')