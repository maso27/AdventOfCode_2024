filename = './Day09/input.txt'
verbose = 3

import pandas as pd

# def is_even(int_in):
#     if int_in % 2 == 0:
#         return True
#     return False

def fragger(file_list_in):
    temp_list = file_list_in.copy()
    fragged_list = []
    
    first_file = temp_list.pop(0)
    fragged_list.append([first_file[0], first_file[1], 0])
    empty_space = first_file[2]
    
    last_file = temp_list.pop()
    file_size = last_file[1]
    
    while len(temp_list) > 0:
        if empty_space == file_size:
            fragged_list.append([last_file[0], file_size, 0])
            
            last_file = temp_list.pop()
            file_size = last_file[1]

            if len(temp_list) >= 1:
                first_file = temp_list.pop(0)
                fragged_list.append([first_file[0], first_file[1], 0])
            empty_space = first_file[2]
            
        elif empty_space > file_size:
            empty_space -= file_size
            fragged_list.append([last_file[0],file_size, 0])
            
            last_file = temp_list.pop()
            file_size = last_file[1]
            
        elif empty_space < file_size:
            file_size -= empty_space
            
            fragged_list.append([last_file[0], empty_space, 0])
            
            first_file = temp_list.pop(0)
            fragged_list.append([first_file[0], first_file[1], 0])
            empty_space = first_file[2]
    fragged_list.append([last_file[0],file_size, 0])

    return fragged_list

def checksum(list_in):
    checksum = 0
    block_index = 0
    for file in list_in:
        file_length = file[1]
        for a in range(file_length):
            checksum += block_index * file[0]
            if verbose >= 5:
                print(f'adding {block_index} * {file[0]} = {block_index * file[0]} to checksum')
            block_index += 1
    return checksum
    
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

if verbose >= 3:
    file_df = pd.DataFrame(file_list, columns=['ID','Size','Empty'])
    print(f'File list:\n{file_df}')

fragged_list = fragger(file_list)

if verbose >= 3:
    file_df = pd.DataFrame(fragged_list, columns=['ID','Size','Empty'])
    print(f'Fragged list:\n{file_df}')
    
drive_checksum = checksum(fragged_list)

print(f'checksum: {drive_checksum}')

# 6447957861015 is too high
# 6447428480341 is too high