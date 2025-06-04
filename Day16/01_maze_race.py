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
        self.location = np.array(start_point, dtype=int)
        self.dir      = np.array([0,1], dtype=int)  # start facing east
        self.path     = [[self.location.copy(),self.dir.copy()]] # latest path explored
        self.history  = [] # every location visited including backsteps
        self.points   = []
        self.finished = False

    def step(self, maze):
        status = 0
        new_location = tuple(self.location + self.dir)
        if maze[new_location] == '#' or new_location in self.history:
            return -1
        elif maze[new_location] == 'E':
            self.finished = True
            status = 1
        self.location = np.array(new_location)
        return status
    
    def check_fwd_left_right(self, maze):
        self.history.append(tuple(self.location))
        # check forward
        status = self.step(maze)
        # check left
        if status < 0: # can't go there
            self.points.append(1000)
            self.dir[0], self.dir[1] = -self.dir[1], self.dir[0] # turn left
            status = self.step(maze)
        # check right
        if status < 0: # can't go there
            self.dir = -self.dir # turn around to check right
            status = self.step(maze)
        # if something worked
        if status == 0:
            self.points.append(1)
            self.path.append([self.location.copy(),self.dir.copy()])
        return status

    def follow_path(self, maze):
        status = 0
        while status == 0:
            status = self.check_fwd_left_right(maze)
        if verbose >= 4:
            print('reached an end point')   
            maze_temp = maze.copy()
            for loc in self.history:
                maze_temp[loc] = ' '
                maze_temp[tuple(self.location)] = 'R'
            show_map(maze_temp)
            input('Press Enter to continue...')
        return status

    def step_back(self, maze):
        while self.check_fwd_left_right(maze) < 0:
            self.history.pop() # clean up last tried location
            last_step     = self.path.pop() # remove last location
            self.location = last_step[0]
            self.dir      = last_step[1]

            # remove points until last wasn't a turn
            last_points = self.points.pop()
            while last_points == 1000 and self.points:
                last_points = self.points.pop()
        self.path.insert(-1, last_step) # final "check_fwd_left_right" already added a value


new_lines = []
with open(filename, 'r') as file:
    for line in file:
        new_lines.append(list(line.rstrip()))
file.close()

maze = np.array(new_lines)
start_arr = np.where(maze=='S')
start_point = [start_arr[0][0], start_arr[1][0]]


full_paths = [] # paths that reach the end

if verbose >= 4:
    show_map(maze)
    print(f'Starting point found at {start_point}')

success = -1
path = Path(start_point)
while path.finished is False:
    success = path.follow_path(maze)
    if success < 0:
        path.step_back(maze)

if verbose >= 3:
    if success == 1:
        print('Reached the end!')
    else:
        print(f'Failed at point{path.location}')

if verbose >= 5:
    maze_temp = maze.copy()
    for loc in path.history:
        maze_temp[loc] = ' '
        maze_temp[tuple(path.location)] = 'R'
    show_map(maze_temp)
full_paths.append(path)
# TODO: continue to find a shorter path
# TODO: make a backstep that expunges history too;j

if verbose >= 1:
    time_stop = time.time()
    print(f'\nTime passed: {time_stop-time_start}')
