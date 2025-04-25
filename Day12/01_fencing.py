filename = './Day12/input.txt'
verbose = 0

# TODO: fix for sample3 'C' value at 4,4
# TODO: fix find_plots to remove diagonals

def build_adjacent(coords):
    adj_list = []
    adj_list.append([coords[0]-1, coords[1]])
    adj_list.append([coords[0]+1, coords[1]])
    adj_list.append([coords[0],   coords[1]-1])
    adj_list.append([coords[0],   coords[1]+1])
    return adj_list

def check_adjacent(coords):
    global counted_spots, garden_map
    plot = []
    adjacents = build_adjacent(coords)
    this_spot = garden_map[coords[1]][coords[0]]
    for adjacent in adjacents:
        if adjacent not in counted_spots:
            next_spot = garden_map[adjacent[1]][adjacent[0]]
            if next_spot == this_spot:
                plot.append(adjacent)
                counted_spots.append(adjacent)
                plot += check_adjacent(adjacent)
    return plot

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



counted_spots = []
for x in range(len(garden_map[0])):
    counted_spots.append([x,0])                # top border
    counted_spots.append([x,len(garden_map)])    # bottom border
for y in range(1,len(garden_map[0])-1): # , start=1):
    counted_spots.append([0,y])                # left border
    counted_spots.append([len(garden_map[0]),y]) # right border

plots_list = []
# for y, row in enumerate(garden_map[1:-1], start=1): # everything but borders
#     for x, spot in enumerate(row[1:-1], start=1): # everything but borders
for y in range(1,len(garden_map)-1):
    for x in range(1,len(garden_map[0])-1):
        if [x,y] not in counted_spots:
            this_plot = check_adjacent([x,y])
            if len(this_plot) == 0: # no adjacents
                this_plot = [[x,y]]
            plots_list.append(this_plot)


if verbose >= 3:
    print('\n - PLOTS FOUND -')
    for plot in plots_list:
        print(plot)

running_total = 0
for plot in plots_list:
    f = find_fences(plot)
    if verbose >= 4:
        print(f'Plot {garden_map[plot[0][1]][plot[0][0]]}: Found {f} fences for plot {plot}')
    running_total += f * len(plot)
print(f'Total cost: {running_total}')