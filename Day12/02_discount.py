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

# def take_sides(plot_in): # calculate the number of fence sides
    # plot_flipped = [i[::-1] for i in plot_in]  # swap y and x in list

    
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