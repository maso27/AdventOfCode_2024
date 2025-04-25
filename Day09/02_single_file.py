filename = './Day09/input.txt'
verbose = 3

import pandas as pd

def build_table(file_list_in):
    files_out = []
    empty_out = []
    file_addr = 0
    for file in file_list_in:
        this_file = [file[0], file[1]]
        files_out.append(this_file + [file_addr])
        file_addr += file[1]
        this_empty = ['x', file[2]]
        empty_out.append(this_empty + [file_addr])
        file_addr += file[2]
    return files_out, empty_out

def move_files(mem_list_in, empty_list_in):
    temp_list = mem_list_in.copy()
    scrambled_list = []
    while len(temp_list) > 0:
        last_file = temp_list.pop()
        for empty_space in empty_list_in:
            if empty_space[2] > last_file[2]: # empty space is higher address
                break
            if last_file[1] <= empty_space[1]: # file size is smaller than empty space
                last_file[2] = empty_space[2] # new address is at beginning of empty space
                empty_space[2] += last_file[1] # empty space now starts later
                empty_space[1] -= last_file[1] # less empty space
                break
        scrambled_list.append(last_file)
    
    sorted_list = sorted(scrambled_list, key=lambda x: x[2])
    return sorted_list

def checksum(list_in):
    checksum = 0
    for file in list_in:
        file_length = file[1]
        block_index = file[2]
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

mem_list, empty_list = build_table(file_list)

sorted_list = move_files(mem_list, empty_list)
if verbose >= 3:
    file_df = pd.DataFrame(mem_list, columns=['ID','Size','Address'])
    print(f'Input list:\n{file_df}')
    sorted_df = pd.DataFrame(sorted_list, columns=['ID','Size','Address'])
    print(f'Sorted list:\n{sorted_df}')
    
drive_checksum = checksum(sorted_list)

print(f'checksum: {drive_checksum}')
