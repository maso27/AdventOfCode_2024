filename = './Day12/input.txt'
verbose = 0

def build_adjacent(coords):
    x, y = coords
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

def check_adjacent(coords):
    global counted_spots, garden_map
    plot = []
    this_spot = garden_map[coords[1]][coords[0]]
    stack = [coords]
    while stack:
        current = stack.pop()
        for adj in build_adjacent(current):
            if adj not in counted_spots:
                if garden_map[adj[1]][adj[0]] == this_spot:
                    plot.append(adj)
                    counted_spots.add(adj)
                    stack.append(adj)
    return plot

def find_fences(plot_in):
    plot_set = set(plot_in)
    fences = 0
    for spot in plot_in:
        for adj in build_adjacent(spot):
            if adj not in plot_set:
                if verbose >= 5:
                    print(f'Fence added at {adj} for {spot}')
                fences += 1
    return fences

# Read and pad map
with open(filename, 'r') as f:
    garden_map = ['.' + line.rstrip() + '.' for line in f]
width = len(garden_map[0])
border = '.' * width
garden_map.insert(0, border)
garden_map.append(border)
height = len(garden_map)

# Initialize counted_spots as set of tuples
counted_spots = set()
for x in range(width):
    counted_spots.add((x, 0))                # top border
    counted_spots.add((x, height - 1))       # bottom border
for y in range(1, height - 1):
    counted_spots.add((0, y))                # left border
    counted_spots.add((width - 1, y))        # right border

plots_list = []
for y in range(1, height - 1):
    for x in range(1, width - 1):
        coord = (x, y)
        if coord not in counted_spots:
            counted_spots.add(coord)
            this_plot = check_adjacent(coord)
            if not this_plot:
                this_plot = [coord]
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