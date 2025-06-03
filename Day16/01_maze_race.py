filename = './Day16/sample.txt'
verbose = 5

import numpy as np
if verbose >= 1:
    import time
    time_start = time.time()

def show_map(map_in):
    for row in map_in:
        for ch in row:
            print(ch, end='')
        print()

class Path:
    def __init__(self, start_point = [0,0]):
        self.history = []
        self.location = np.array(start_point, dtype=int)
        self.dir = np.array([1,0], dtype=int)  # start facing east
        self.points = 0

    def turn(self, direction = 'right'):
        if direction == 'right':
            self.dir[0], self.dir[1] = -self.dir[1], self.dir[0]
        elif direction == 'left':
            self.dir[0], self.dir[1] = self.dir[1], -self.dir[0]
        else:
            raise ValueError("Direction must be 'right' or 'left'")
        self.points += 1000

    def step(self, maze):
        self.history.append(tuple(self.location))
        new_location = tuple(self.location + self.dir)
        if maze[new_location] == '#' or new_location in self.history:
            return -1
        elif maze[new_location] == 'E':
            self.points += 1
            return 1
        self.points += 1
        self.location = np.array(new_location)
        return 0

    def next_step(self, maze):
        status = self.step(maze)
        num_turns = 0
        while status < 0 and num_turns < 4:
            # TODO: redo to look left and right, not just rotations
            num_turns += 1
            self.turn()
            status = self.step(maze)
        return status
    
    def follow_path(self, maze):
        status = 0
        while status == 0:
            status = self.next_step(maze)
        return status
    
    def step_back(self, maze):
        # TODO: in a failed path, step back to the last point and continue
        return 0
    
new_lines = []
with open(filename, 'r') as file:
    for line in file:
        new_lines.append(list(line.rstrip()))
file.close()

maze = np.array(new_lines)
start_arr = np.where(maze=='S')
start_point = [start_arr[0][0], start_arr[1][0]]
paths = [Path(start_point)]

full_paths = [] # paths that reach the end

if verbose >= 4:
    show_map(maze)
    print(f'Starting point found at {start_point}')

success = paths[0].follow_path(maze)

if verbose >= 3:
    if success == 1:
        print('Reached the end!')
    else:
        print(f'Failed at point{paths[0].location}')

if verbose >= 5:
    maze_temp = maze.copy()
    for loc in paths[0].history:
        maze_temp[loc] = ' '
        maze_temp[tuple(paths[0].location)] = 'R'
    show_map(maze_temp)
    
if verbose >= 1:
    time_stop = time.time()
    print(f'\nTime passed: {time_stop-time_start}')
