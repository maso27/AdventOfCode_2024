filename = './Day12/input.txt'
verbose = 0

def build_adjacent(coords):
    x, y = coords
    return [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]

def check_adjacent(coords):
    global counted_spots, garden_map
    plot = []
    this_spot = garden_map[coords[1]][coords[0]]

    adjacents = build_adjacent(coords)
    for adjacent in adjacents:
        if tuple(adjacent) not in counted_spots:
            next_spot = garden_map[adjacent[1]][adjacent[0]]
            if next_spot == this_spot:
                plot.append(adjacent)
                counted_spots.add(tuple(adjacent))
                plot += check_adjacent(adjacent)
    return plot

def find_fences(plot_in):
    spots_n = []    # all northern fences
    spots_s = []    # ''  southern ''
    spots_e = []    # ''  eastern  ''
    spots_w = []    # ''  western  ''

    for spot in plot_in:
        x, y = spot
        if [x,y-1] not in plot_in:
            spots_e.append([x,y-1])
        if [x,y+1] not in plot_in:
            spots_w.append([x,y+1])
        if [x-1,y] not in plot_in:
            spots_n.append([x-1,y])
        if [x+1,y] not in plot_in:
            spots_s.append([x+1,y])

    # sort vertical fences
    spots_n.sort(key=lambda x: x[1]) # sort by y first
    spots_n.sort()                   # sort by x second
    spots_s.sort(key=lambda x: x[1]) # sort by y first
    spots_s.sort()                   # sort by x second

    # sort horizontal fences
    spots_e.sort()                   # sort by x first
    spots_e.sort(key=lambda x: x[1]) # sort by y second
    spots_w.sort()                   # sort by x first
    spots_w.sort(key=lambda x: x[1]) # sort by y second

    if verbose >= 4:
        print(f'Horizontal Fence: {spots_e+spots_w}')
        print(f'Vertical Fence:   {spots_n+spots_s}')

    num_fences = 0
    for spot in spots_e:
        x, y = spot
        if [x+1,y] not in spots_e:
            num_fences += 1
    for spot in spots_w:
        x, y = spot
        if [x+1,y] not in spots_w:
            num_fences += 1
    for spot in spots_n:
        x, y = spot
        if [x,y+1] not in spots_n:
            num_fences += 1
    for spot in spots_s:
        x, y = spot
        if [x,y+1] not in spots_s:
            num_fences += 1

    return num_fences


# Read file more efficiently
with open(filename, 'r') as f:
    garden_map = ['.'+line.rstrip()+'.' for line in f]

# Get dimensions once
width = len(garden_map[0])
border = '.' * width
garden_map.insert(0, border)
garden_map.append(border)
height = len(garden_map)

# Use set for O(1) lookup
counted_spots = set()
counted_spots.update((x, 0) for x in range(width))
counted_spots.update((x, height-1) for x in range(width))
counted_spots.update((0, y) for y in range(height))
counted_spots.update((width-1, y) for y in range(height))

plots_list = []
for y in range(1,len(garden_map)-1):
    for x in range(1,len(garden_map[0])-1):
        if (x,y) not in counted_spots:
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
