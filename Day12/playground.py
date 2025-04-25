# test_map = [['.','.','.','.'],
#             ['.','A','A','.'],
#             ['.','A','A','.'],
#             ['.','.','.','.']]
test_map = [['.','.','.','.','.'],
            ['.','A','A','B','.'],
            ['.','A','A','B','.'],
            ['.','C','C','B','.'],
            ['.','.','.','.','.']]
test_locations = [[1,1],[1,2],[2,1],[2,2]]

adj_horiz = []
for row in test_map:
    last_val = row[0]
    this_row = []
    for pixel in row[1:]:
        if pixel == last_val and pixel != '.':
            this_row.append('-')
        else:
            this_row.append('.')
        last_val = pixel
    adj_horiz.append(this_row)

print('\n adj_horiz:')
for row in adj_horiz:
    print(row)
    
adj_vert  = []
last_row = test_map[0]
for row in test_map[1:]:
    this_row = []
    for a, pixel in enumerate(row):
        if pixel == last_row[a] and pixel != '.':
            this_row.append('|')
        else:
            this_row.append('.')
    last_row = row
    adj_vert.append(this_row)

print('\n adj_vert')
for row in adj_vert:
    print(row)

# output:
#  adj_horiz:
# ['.', '.', '.', '.']
# ['.', '-', '.', '.']
# ['.', '-', '.', '.']
# ['.', '-', '.', '.']
# ['.', '.', '.', '.']

#  adj_vert
# ['.', '.', '.', '.', '.']
# ['.', '|', '|', '|', '.']
# ['.', '.', '.', '|', '.']
# ['.', '.', '.', '.', '.']