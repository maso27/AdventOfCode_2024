filename = './Day12/input.txt'
verbose = 0

def build_adjacent(coords):
    x, y = coords
    return [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]

def check_adjacent(coords):
    global counted_spots, garden_map
    plot = []
    this_spot = garden_map[coords[1]][coords[0]]
    stack = [coords]
    
    while stack:
        current = stack.pop()
        adjacents = build_adjacent(current)
        for adjacent in adjacents:
            adj_x, adj_y = adjacent
            if tuple(adjacent) not in counted_spots:
                if garden_map[adj_y][adj_x] == this_spot:
                    plot.append(adjacent)
                    counted_spots.add(tuple(adjacent))
                    stack.append(adjacent)
    return plot

def find_fences(plot_in):
    plot_set = {tuple(spot) for spot in plot_in}
    return sum(1 for spot in plot_in 
              for adj in build_adjacent(spot) 
              if tuple(adj) not in plot_set)

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
for y in range(1, height-1):
    for x in range(1, width-1):
        if (x, y) not in counted_spots:
            this_plot = check_adjacent([x, y])
            if not this_plot:
                this_plot = [[x, y]]
            plots_list.append(this_plot)

running_total = sum(find_fences(plot) * len(plot) for plot in plots_list)
print(f'Total cost: {running_total}')