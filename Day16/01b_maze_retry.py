filename = './Day16/sample.txt'
verbose = 5

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
        branches.remove(tuple(self.dir))
        for direction in branches.copy():
            branch = self.location + direction
            if self.maze[tuple(branch)] == '#':
                branches.remove(direction)

        self.path     = [{'location': self.location.copy(),     # latest location explored
                          'dir':      self.dir.copy(),          # latest direction explored
                          'branches': branches}]                # branches left unexplored
        
        self.points   = []
        self.lowest_score = sys.maxsize

    def show_map(self):
        maze_temp = self.maze.copy()
        for step in self.path:
            maze_temp[tuple(step['location'])] = ' '
        maze_temp[tuple(self.location)] = 'R'

        for row in maze_temp:
            for ch in row:
                print(ch, end='')
            print()

    def look_and_step(self):
        branches = self.cardinals.copy()
        branches.remove(tuple(self.dir*-1)) # don't look where you've been
        for direction in branches.copy():
            if self.maze(tuple(self.location + direction)) == '#':
                branches.remove(direction)
        if branches:
            # TODO: try to go forward (maybe need to rethink a bit?)
            # TODO: add points as needed
            # TODO: update location
            # TODO: update direction
            # TODO: update path
            pass

new_lines = []
with open(filename, 'r', encoding="utf8") as file:
    for line in file:
        new_lines.append(list(line.rstrip()))
file.close()

maze = np.array(new_lines)

maze_path = Path(maze)
maze_path.show_map()

# TODO: Check all turns and mark branch points
# TODO: Advance through one path at a time, incrementing points
# TODO: Implement backtracking and blocking tried branches
# TODO: Stop a path if it's more expensive than best so far


if verbose >= 1:
    time_stop = time.time()
    print(f'\nTime passed: {time_stop-time_start}')