filename = './Day12/sample3.txt'
verbose = 4

# TODO: fix for sample3 'C' value at 4,4
# TODO: fix find_plots to remove diagonals

def build_adjacent(coords):
    adj_list = []
    adj_list.append([coords[0]-1, coords[1]])
    adj_list.append([coords[0]+1, coords[1]])
    adj_list.append([coords[0],   coords[1]-1])
    adj_list.append([coords[0],   coords[1]+1])
    return adj_list

def find_plots(map_in):
    plots_list = []
    for y, row in enumerate(map_in[1:-1], start=1): # everything but borders
        for x, spot in enumerate(row[1:-1], start=1): # everything but borders
            is_in_plot = False
            for plot in plots_list:
                for yy in range(y-1, y+2): # check 1 down and 1 up
                    for xx in range(x-1, x+2): # check 1 left and 1 right
                        if map_in[y][x] == map_in[yy][xx] and [xx,yy] in plot:
                            plot.append([x,y])
                            is_in_plot = True
                            break
                    if is_in_plot:
                        break
                if is_in_plot:
                    break
            if not is_in_plot:
                plots_list.append([[x,y]])
    return plots_list

def find_fences(plot_in):
    fences = 0
    for spot in plot_in:
        adjacents = build_adjacent(spot)
        for adjacent in adjacents:
            if adjacent not in plot_in:
                if verbose >= 5:
                    print(f'Fence added at {adjacent} for {spot}')
                fences += 1
    return fences

f = open(filename, 'r')
new_lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

garden_map = []
for line in new_lines: # clean \n's
    this_line = line.rstrip()
    garden_map.append('.' + this_line + '.')
    
# put . around edge
border = '.' * len(garden_map[0])
garden_map.insert(0, border)
garden_map.append(border)

plots = find_plots(garden_map)

if verbose >= 3:
    print('\n - PLOTS FOUND -')
    for plot in plots:
        print(plot)

running_total = 0
for plot in plots:
    f = find_fences(plot)
    if verbose >= 4:
        print(f'Plot {garden_map[plot[0][1]][plot[0][0]]}: Found {f} fences for plot {plot}')
    running_total += f * len(plot)
print(f'Total cost: {running_total}')