# test_map = [['.','.','.','.','.'],
#             ['.','A','A','B','.'],
#             ['.','A','A','B','.'],
#             ['.','C','C','C','.'],
#             ['.','.','.','.','.']]

test_map = [['.','.','.','.','.'],
            ['.','A','A','B','.'],
            ['.','A','A','C','.'],
            ['.','C','C','C','.'],
            ['.','.','.','.','.']]

def build_adjacent(coords):
    adj_list = []
    adj_list.append([coords[0]-1, coords[1]])
    adj_list.append([coords[0]+1, coords[1]])
    adj_list.append([coords[0],   coords[1]-1])
    adj_list.append([coords[0],   coords[1]+1])
    return adj_list

def check_adjacent(coords):
    global counted_spots, test_map
    plot = []
    adjacents = build_adjacent(coords)
    this_spot = test_map[coords[1]][coords[0]]
    for adjacent in adjacents:
        if adjacent not in counted_spots:
            next_spot = test_map[adjacent[1]][adjacent[0]]
            if next_spot == this_spot:
                plot.append(adjacent)
                counted_spots.append(adjacent)
                plot += check_adjacent(adjacent)
    return plot

counted_spots = []
for x in range(len(test_map[0])):
    counted_spots.append([x,0])                # top border
    counted_spots.append([x,len(test_map)])    # bottom border
for y in range(1,len(test_map[0])-1): # , start=1):
    counted_spots.append([0,y])                # left border
    counted_spots.append([len(test_map[0]),y]) # right border

plots_list = []
# for y, row in enumerate(test_map[1:-1], start=1): # everything but borders
#     for x, spot in enumerate(row[1:-1], start=1): # everything but borders
for y in range(1,len(test_map)-1):
    for x in range(1,len(test_map[0])-1):
        if [x,y] not in counted_spots:
            this_plot = check_adjacent([x,y])
            if len(this_plot) == 0: # no adjacents
                this_plot = [[x,y]]
            plots_list.append(this_plot)


for plot in plots_list:
    print(plot)

# Old output:
# [[1, 1], [2, 1], [1, 2], [2, 2]]
# [[3, 1], [3, 2], [3, 3]]
# [[1, 3], [2, 3]]


# Broken output:
# [[1, 1], [2, 1], [1, 2], [2, 2]]
# [[3, 1]]
# [[3, 2], [2, 3], [3, 3]]
# [[1, 3]]