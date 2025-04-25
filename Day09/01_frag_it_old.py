filename = './Day09/sample.txt'
verbose = 5

import pandas as pd

# def is_even(int_in):
#     if int_in % 2 == 0:
#         return True
#     return False

def fragger(file_list_in):
    # TODO: move files from the end to fill earlier gaps

    return file_list_in

f = open(filename, 'r')
# new_lines = f.readlines() # reading all lines
line = f.readline()  # reading one line
f.close()

line = line.rstrip()

num_files = int(len(line) / 2)

file_list = []
for a in range(num_files):
    file_size = int(line[a*2])
    empty_blocks = int(line[a*2+1])
    file_list.append([a, file_size, empty_blocks]) # file id, file size, empty blocks after
file_list.append([num_files, int(line[-1]), 0]) # last file

file_df = pd.DataFrame(file_list, columns=['ID','Size','Empty'])

if verbose >= 5:
    print(f'File list: {file_df}')