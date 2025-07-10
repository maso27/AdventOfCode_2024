filename = './Day16/input.txt'
verbose = 1

import sys
import numpy as np
if verbose >= 1:
    import time
    time_start = time.time()


class Path:
    def __init__(self, maze = np.array([['S','E']])):
        self.maze        = maze

        self.cardinals = {(0,1),(-1,0),(0,-1),(1,0)} # E, N, W, S (set)

        start_arr        = np.where(self.maze == 'S')
        self.start_point = [start_arr[0][0], start_arr[1][0]]
        end_arr          = np.where(self.maze == 'E')
        self.end_point   = [end_arr[0][0], end_arr[1][0]]

        self.location = np.array(self.start_point, dtype=int)
        self.dir      = np.array([0,1], dtype=int)  # begin facing east

        # check for possible starting directions
        branches = self.cardinals.copy()
        for direction in branches.copy():
            branch = self.location + direction
            if self.maze[tuple(branch)] == '#':
                branches.remove(direction)

        self.path     = [{'location': self.location.copy(),     # latest location explored
                          'dir':      self.dir.copy(),          # latest direction explored
                          'branches': branches}]                # branches left unexplored
        
        self.points   = []
        self.paths = [] # all successful paths
        self.lowest_score = sys.maxsize

        self.finished = False # Finished exploring all paths

    def show_map(self):
        maze_temp = self.maze.copy()
        for step in self.path:
            maze_temp[tuple(step['location'])] = ' '
        maze_temp[tuple(self.location)] = 'R'

        for row in maze_temp:
            for ch in row:
                print(ch, end='')
            print()

    def step_and_look(self):
        branches = self.path[-1]['branches'].copy()

        # if sum(self.points) > self.lowest_score: # too expensive, abandon this path
        #     self.backtrack()
        #     return False
        
        # 1. take a step
        if tuple(self.dir) in branches: # can go forward
            self.location += self.dir
            self.points.append(1)
        else: # can't go forward, check branches 
            self.dir = np.array(branches.pop()) # take a branch
            self.location += self.dir
            self.points.append(1001) # a turn and a step

        # 2. remove the direction as a path taken
        self.path[-1]['branches'].remove(tuple(self.dir))
        
        # 3. Check for end point
        if self.location.tolist() == self.end_point:
            # self.path.append({'location': self.location.copy(),
            #                   'dir':      self.dir.copy(),
            #                   'branches': {}})
            # self.points.append(0) # keeping backtracking simple
            return True
        
        # 4. Check for new branches
        branches = self.cardinals.copy()
        branches.remove(tuple(self.dir*-1)) # don't look where you've been
        for direction in branches.copy():
            for step in self.path: # prevent loops
                if np.array_equal((self.location + direction), step['location']):
                    branches.remove(direction)
                    continue
            if self.maze[tuple(self.location + direction)] == '#':
                branches.remove(direction)
        if branches:
            self.path.append({'location': self.location.copy(),     # latest location explored
                              'dir':      self.dir.copy(),          # latest direction explored
                              'branches': branches})                # branches left unexplored          
        else: # no way forward, backtrack
            self.backtrack()
        
        return False

    def backtrack(self):
        while not self.path[-1]['branches']: # backtrack until there's an unexplored branch
            if len(self.path) == 1: # done with all paths
                self.finished = True
                return
            self.points.pop() # remove points for the last step
            self.path.pop()   # remove the last step
        self.location = self.path[-1]['location'].copy()
        self.dir      = self.path[-1]['dir'].copy()
        self.points.pop() # one more points removal

new_lines = []
with open(filename, 'r', encoding="utf8") as file:
    for line in file:
        new_lines.append(list(line.rstrip()))
file.close()

maze = np.array(new_lines)

maze_path = Path(maze)
maze_path.show_map()

while not maze_path.finished:
    found_end = maze_path.step_and_look()
    if found_end:
        maze_path.paths.append(maze_path.path.copy())
        if sum(maze_path.points) < maze_path.lowest_score:
            maze_path.lowest_score = sum(maze_path.points)
            print(f'New best path found with score {maze_path.lowest_score}!')
        if verbose >= 4:    
            maze_path.show_map()
            input('Press Enter to continue...')
        maze_path.backtrack()  # backtrack to the last step

print(f'\n Cheapest path score: {maze_path.lowest_score}')

if verbose >= 1:
    time_stop = time.time()
    print(f'\nTime passed: {time_stop-time_start}')