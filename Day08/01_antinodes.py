filename = './Day08/input.txt'
verbose = 3

f = open(filename, 'r')
new_lines = f.readlines() # reading all lines
# line = f.readline()  # reading one line
f.close()

lines = []
for line in new_lines: # clean \n's
    lines.append(line.rstrip())

def scan_for_freqs(map):
    freq_list = ['.']
    for scan_line in map:
        for pixel in scan_line:
            if pixel not in freq_list:
                if verbose >= 3:
                    print(f'Found frequency {pixel}')
                freq_list.append(pixel)
    return freq_list[1:] # omit the dots

def find_freq_locs(map, freq):
    freq_locs = []
    for y, line in enumerate(map):
        for x, pixel in enumerate(line):
            if pixel == freq:
                freq_locs.append([x,y])
                if verbose >= 5:
                    print(f'Frequency {freq} found at {[x,y]}')
    return freq_locs

def find_nodes(map, freqs):
    limits = [len(lines[-1])-1, len(lines)-1]
    if verbose == 5:
        print(f'\n Map limits: {limits}\n')
    node_locs = []
    for freq in freqs:
        freq_locs = find_freq_locs(map,freq)
        while len(freq_locs) > 1:
            this_loc = freq_locs.pop()
            for freq_loc in freq_locs:
                if verbose >= 4:
                    print(f'Comparing {this_loc} with {freq_loc}')
                slope = [x - y for x, y in zip(this_loc, freq_loc)]
                node_1_loc = [x + y for x, y in zip(this_loc, slope)]
                node_2_loc = [x - y for x, y in zip(freq_loc, slope)]
                if verbose >= 4:
                    print(f'Found nodes for frequency {freq} at {node_1_loc} and {node_2_loc}')
                if (node_1_loc[0] >= 0 and node_1_loc[0] <= limits[0]) and (node_1_loc[1] >= 0 and node_1_loc[1] <= limits[1]) and (node_1_loc not in node_locs):
                    if verbose >= 3:
                        print(f'Adding node for frequency {freq} at {node_1_loc}')
                    node_locs.append(node_1_loc)
                if (node_2_loc[0] >= 0 and node_2_loc[0] <= limits[0]) and (node_2_loc[1] >= 0 and node_2_loc[1] <= limits[1]) and (node_2_loc not in node_locs):
                    if verbose >= 3:
                        print(f'Adding node for frequency {freq} at {node_2_loc}')
                    node_locs.append(node_2_loc)

    return node_locs
        
frequencies = scan_for_freqs(lines)
node_locs = find_nodes(lines, frequencies)
if verbose >= 2:
    print(f'Nodes found at {node_locs}')

print(f'Number of nodes: {len(node_locs)}')
