filename = './Day12/sample1.txt'
verbose = 5

def build_adjacent_spots(coords):
    adj_list = []
    adj_list.append([coords[0]-1, coords[1]])
    adj_list.append([coords[0]+1, coords[1]])
    adj_list.append([coords[0],   coords[1]-1])
    adj_list.append([coords[0],   coords[1]+1])
    return adj_list

def check_adjacent(coords):
    global counted_spots, garden_map
    plot = []
    adjacents = build_adjacent_spots(coords)
    this_spot = garden_map[coords[1]][coords[0]]
    for adjacent in adjacents:
        if adjacent not in counted_spots:
            next_spot = garden_map[adjacent[1]][adjacent[0]]
            if next_spot == this_spot:
                plot.append(adjacent)
                counted_spots.append(adjacent)
                plot += check_adjacent(adjacent)
    return plot

# def take_sides(plot_in): # calculate the number of fence sides
    # plot_flipped = [i[::-1] for i in plot_in]  # swap y and x in list

    
def find_fences(plot_in):
    fence_spots = []
    for spot in plot_in:
        adjacents = build_adjacent_spots(spot)
        for adjacent in adjacents:
            if adjacent not in plot_in:
                if verbose >= 5:
                    print(f'Fence added at {adjacent} for {spot}')
                fence_spots.append(adjacent)
    
    fence_sort = sorted(fence_spots)
    if verbose >= 4:
        print(f'Sorted Fence: {fence_sort}')
    vert_lengths = []
    misc = []
    while len(fence_sort) > 0:
        temp_loc = fence_sort.pop(0)
        if temp_loc[0] == fence_sort[0][0] and temp_loc[1] == fence_sort[0][1] - 1:
            if verbose >= 5:
                print(f'Vertical fence at {temp_loc} and {fence_sort[0]}')
            vert_lengths.append(temp_loc)
        else:
            misc.append(temp_loc)
        
    return len(fence_sort)

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