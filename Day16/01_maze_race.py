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
    def __init__(self, maze = np.array([['S','E']])):
        self.maze        = maze
        
        start_arr        = np.where(self.maze == 'S')
        self.start_point = [start_arr[0][0], start_arr[1][0]]
        end_arr          = np.where(self.maze == 'E')
        self.end_point   = [end_arr[0][0], end_arr[1][0]]

        self.location = np.array(self.start_point, dtype=int)
        self.dir      = np.array([0,1], dtype=int)  # start facing east
        self.path     = [[self.location.copy(),self.dir.copy()]] # latest path explored
        self.history  = [] # every location visited including backsteps
        self.points   = []
        self.finished = False

    def step(self):
        status = 0
        new_location = tuple(self.location + self.dir)
        if self.maze[new_location] == '#' or new_location in self.history:
            return -1
        elif new_location == tuple(self.end_point):
            self.finished = True
            return 1
        self.location = np.array(new_location)
        return status
    
    def check_fwd_left_right(self):
        self.history.append(tuple(self.location))
        # check forward
        status = self.step()
        # check left
        if status < 0: # can't go there
            self.points.append(1000)
            self.dir[0], self.dir[1] = -self.dir[1], self.dir[0] # turn left
            status = self.step()
        # check right
        if status < 0: # can't go there
            self.dir = -self.dir # turn around to check right
            status = self.step()
        # if something worked
        if status == 0:
            self.points.append(1)
            self.path.append([self.location.copy(),self.dir.copy()])
        return status

    def follow_path(self):
        status = 0
        while status == 0:
            status = self.check_fwd_left_right()
        if verbose >= 4:
            print('reached an end point')   
            maze_temp = self.maze.copy()
            for loc in self.history:
                maze_temp[loc] = ' '
            maze_temp[tuple(self.location)] = 'R'
            show_map(maze_temp)
            input('Press Enter to continue...')
        return status

    def step_back(self):
        while self.check_fwd_left_right() < 0:
            self.history.pop() # clean up last tried location
            if self.finished:
                self.history.pop() # not blocking old locations, but blocking this one
                self.history.append(self.location) # preventing us from just using the same old path
            last_step     = self.path.pop() # remove last location
            self.location = last_step[0]
            self.dir      = last_step[1]

            # remove points until last wasn't a turn
            last_points = self.points.pop()
            while last_points == 1000 and self.points:
                last_points = self.points.pop()
        self.finished = False # for when we're looking for another path
        self.path.insert(-1, last_step) # final "check_fwd_left_right" already added a value


new_lines = []
with open(filename, 'r') as file:
    for line in file:
        new_lines.append(list(line.rstrip()))
file.close()

maze = np.array(new_lines)

# set up to start in any cardinal direction
cardinals = {'east': {}, 'west': {}, 'north': {}, 'south': {}}
cardinals['east']['dir']  = np.array([0, 1], dtype=int)
cardinals['west']['dir']  = np.array([0,-1], dtype=int)
cardinals['north']['dir'] = np.array([-1,0], dtype=int)
cardinals['south']['dir'] = np.array([ 1,0], dtype=int)
cardinals['east']['points']  = [0]
cardinals['west']['points']  = [1000, 1000]
cardinals['north']['points'] = [1000]
cardinals['south']['points'] = [1000]


full_paths = [] # paths that reach the end

for _,direction in cardinals.items():

    maze_path        = Path(maze)
    maze_path.dir    = direction['dir']
    maze_path.points = direction['points']
    
    success = -1
    
    while maze_path.finished is False:
        success = maze_path.follow_path()
        if success < 0:
            maze_path.step_back()
    full_paths.append(maze_path)

    # maze_path.step_back()
    # maze_path.finished = False # reset to try again
    # while maze_path.finished is False:
    #     success = maze_path.follow_path()
    #     if success < 0:
    #         maze_path.step_back()

    if verbose >= 3:
        if success == 1:
            print('Reached the end!')
        else:
            print(f'Failed at point{maze_path.location}')

    if verbose >= 5:
        maze_temp = maze_path.maze.copy()
        for loc in maze_path.history:
            maze_temp[loc] = ' '
            maze_temp[tuple(maze_path.location)] = 'R'
        show_map(maze_temp)

# TODO: continue to find a shorter path
# TODO: make a backstep that expunges history too

if verbose >= 1:
    time_stop = time.time()
    print(f'\nTime passed: {time_stop-time_start}')
