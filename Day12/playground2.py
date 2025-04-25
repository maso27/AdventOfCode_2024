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

temp_map = test_map.copy()

plots_list = []
for y, row in enumerate(test_map[1:-1], start=1): # everything but borders
    for x, spot in enumerate(row[1:-1], start=1): # everything but borders
        is_in_plot = False
        for plot in plots_list:
            for yy in range(y-1, y+2): # check 1 down and 1 up
                for xx in range(x-1, x+2): # check 1 left and 1 right
                    if test_map[y][x] == test_map[yy][xx] and [xx,yy] in plot:
                        plot.append([x,y])
                        is_in_plot = True
                        break
                if is_in_plot:
                    break
            if is_in_plot:
                break
        if not is_in_plot:
            plots_list.append([[x,y]])

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