import labyrinth2 as lab
import random as ran
import numpy as np
import os
import sys
import time
import copy
import math

points = {
    'visible': ['F', 'm', 'p', 'S'],
    'end': []
}

matrixes = {
    'open': [],
    'hidden': [],
    'size': 16
}

memory = {
    'distances': [],
    'forks': [],
    'moved': [],
    'moved_forks': [],
    'dead_ends': [],
    'last_fork': []
}


class Bot:
    '''And here's our little guy to do the maze solving for us.'''
    def __init__(self, matrix, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.distance = 0
        self.clear()
        self.clear_memory()
        matrix[self.y][self.x] = 'B'
        self.show_maze(matrix)
        print("Let's go!")
        time.sleep(2)
        self.main(matrix, points['end'])

    
    def main(self, matrix, end):
        '''Main logic loop'''
        while (self.x, self.y) != end:
            self.clear()
            memory['moved'].append((self.x, self.y))
            self.distance = self.calculate_distance(self.x, self.y, *end)
            if self.check_moveable_tile(matrix, end):
                next_tile = self.check_lowest_tile()
                mem_tile = self.check_memory(next_tile)
                if next_tile != mem_tile:
                    if mem_tile[0] not in memory['moved_forks']: 
                        memory['moved'] = [(self.x, self.y)]
                        memory['forks'] = []
                        self.show_maze(matrix)
                        print(f'Going back to {mem_tile[0]}')
                        time.sleep(1)
                        next_tile = (self.main(matrix, mem_tile[0]), 0)
                        self.clear()
                    else:
                        for value in memory['forks']:
                            b, _ = value
                            memory['moved_forks'].append(b)
                        memory['forks'].remove(mem_tile)
                        print("I've tried that fork before, I'm pushing forwards.")        
            else:
                print('Dead end, retracing steps.')
                if (self.x, self.y) in memory['last_fork']:
                    memory['last_fork'].remove((self.x, self.y))
                next_tile = (self.retrace(matrix), 0)

            matrix[self.y][self.x] = matrixes['hidden'][self.y][self.x]
            self.x, self.y = next_tile[0]
            matrix[self.y][self.x] = 'B'
            self.show_maze(matrix)
            time.sleep(1)
        memory['forks'] = []
        memory['moved_forks'].append((self.x, self.y))
        return self.x, self.y


    def check_moveable_tile(self, matrix, end):
        next_tiles = []
        for y in range(self.y - 1, self.y + 2, 2):
            try:
                if matrix[y][self.x] in points['visible'] and (self.x, y) not in memory['moved'] and (self.x, y) not in memory['dead_ends'] and y > -1:
                    next_tiles.append((self.x, y))
            except IndexError:
                continue
        for x in range(self.x - 1, self.x + 2, 2):
            try:
                if matrix[self.y][x] in points['visible'] and (x, self.y) not in memory['moved'] and (x, self.y) not in memory['dead_ends'] and x > -1:
                    next_tiles.append((x, self.y))
            except IndexError:
                continue
        
        if len(next_tiles) >= 2 and (self.x, self.y) not in memory['last_fork']:
                memory['last_fork'].append((self.x, self.y))
        
        memory['distances'] = []
        for tiles in next_tiles:
            memory['distances'].append((tiles, self.calculate_distance(*tiles, *end)))
        if not memory['distances']:
            return False
        return True


    def draw_matrix(self, matrix):
        matrix[self.y][self.x] = matrixes['hidden'][self.y][self.x]


    def retrace(self, matrix):
        memory['moved'].pop(-1)
        while (self.x, self.y) not in memory['last_fork']:
            memory['dead_ends'].append((self.x, self.y))
            matrix[self.y][self.x] = matrixes['hidden'][self.y][self.x]
            self.x, self.y = memory['moved'].pop(-1)
            matrix[self.y][self.x] = 'B'
            self.show_maze(matrix)
            time.sleep(1)
            self.clear()
        for value in memory['forks']:
            cord, _ = value
            if cord in memory['dead_ends']:
                memory['forks'].remove(value)
        return self.x, self.y


    @staticmethod
    def check_memory(next_tile):
        try:
            member_min = min(memory['forks'], key = lambda t: t[1])
            if member_min[1] < next_tile[1]:
                return member_min
            return next_tile
        except ValueError:
            return next_tile

    @staticmethod    
    def check_lowest_tile():
        min_tile = min(memory['distances'], key = lambda t: t[1])
        memory['distances'].remove(min_tile)
        for value in memory['distances']:
            memory['forks'].append(value)
        return min_tile

    @staticmethod
    def calculate_distance(x, y, end_x, end_y):
        return math.sqrt((end_x - x)**2 + (end_y - y)**2)

    @staticmethod
    def clear():
        '''Function for clearing the cmd.'''
        os.system('cls')

    @staticmethod
    def show_maze(matrix):
        '''Function for diplaying the maze.'''
        print(np.matrix(matrix))

    @staticmethod
    def clear_memory():
        for value in memory:
            memory[value] = []


try:
    while True:
        maze = lab.Matrix(matrixes['size'], matrixes['size'])
        points['end'] = lab.coordinates['end']
        matrixes['open'] = maze.matrix
        matrixes['hidden'] = copy.deepcopy(matrixes['open'])
        Bot(matrixes['open'], lab.coordinates['start'][0], lab.coordinates['start'][1])
        print("Let's go again!")
        time.sleep(3)
except KeyboardInterrupt:
    print(memory)
    print(points['end'])
    Bot.show_maze(matrixes['open'])
    print(matrixes['hidden'])



"""#branch used for debugging
try:
    debug_matrix = 
    while True:
        points['end'] = (13, 11)
        matrixes['open'] = debug_matrix
        matrixes['hidden'] = copy.deepcopy(matrixes['open'])
        Bot(matrixes['open'], 0, 11)
        print("Let's go again!")
        time.sleep(3)
except KeyboardInterrupt:
    print(memory)
    Bot.show_maze(matrixes['open'])
    print(matrixes['hidden'])"""