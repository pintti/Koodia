import labyrinth2 as lab
import random as ran
import numpy as np
import os
import sys
import time
import copy
import math

matrixes = {
    'size': [10, 10],
    'open': [],
    'hidden': []
}

points = {
    'end': [],
    'stop': [],
    'start': [],
    'continue': 'y',
    'visible': ['F', 'm', 'S', 'p'],
    'pickaxe': 0,
    'pickedup': 0,
    'torch': 3
}  

memory = {
    'forks': [],
    'moved': [],
    'distance': 0,
    'distance2': 0,
    'turns': []
}


class Bot:
    '''This lil fella is going to be running through a labyrinth trying to solve it. Godspeed lil' bot, godspeed.'''
    def __init__(self, matrix):
        self.x = points['start'][0]
        self.y = points['start'][1]
        self.main(matrix)


    def main(self, matrix):
        while (self.x, self.y) != points['end']:
            self.move(matrix, points['end'])
        print('I got to the end!')
        print("Let's go deeper?")
        input()

    
    def move(self, matrix, end):
        clear()
        memory['distance'] = self.calculate_distance(self.x, self.y, *end)
        check = self.check_moveable_tile(matrix, end)
        if check == 1:
            memory['moved'].append((self.x, self.y))

        elif check == 2:
            memory['moved'].append((self.x, self.y))

        elif check == 0:
            print('Gotta turn around')
            if (self.x, self.y) not in memory['turns']:
                memory['turns'].append((self.x, self.y))
                memory['moved'] = []
                if memory['forks'] != []:
                    self.remember_fork(memory['forks'])
                    memory['forks'] = []
                    memory['moved'].append((self.x, self.y))
                    self.move(matrix, points['stop'])
                else:
                    memory['moved'].append((self.x, self.y))
            else:
                print("I've been here before.")
                print("I'm going to need the pickaxe.")
                show_maze(matrix)
                print(memory['forks'])
                input()

        matrix[self.y][self.x] = 'B'
        show_maze(matrix)
        time.sleep(1)


    def calculate_distance(self, x, y, end_x, end_y):
        '''Calculates the distance to the wanted point. x and y are the points where Bot is right now, end_x and end_y is
        where the bot wants to go.'''
        distance = math.sqrt((end_x - x)**2 + (end_y - y)**2)
        return distance


    def check_moveable_tile(self, matrix, end):
        good_tiles = []
        for y in range(self.y - 1, self.y + 2, 2):
            try:
                if matrix[y][self.x] in points['visible'] and (self.x, y) not in memory['moved'] and y >= 0:
                    good_tiles.append((self.x, y))
            except IndexError:
                continue
        for x in range(self.x - 1, self.x + 2, 2):
            try:
                if matrix[self.y][x] in points['visible'] and (x, self.y) not in memory['moved'] and x >= 0:
                    good_tiles.append((x, self.y))
            except IndexError:
                continue
        if len(good_tiles) > 1:
            print('A fork in the path.')
            solution = self.solve_fork(matrix, good_tiles, end)
            if solution == 2:
                return 2
            elif solution == 0:
                return 0

        elif len(good_tiles) == 1:
            matrix[self.y][self.x] = 'm'
            self.x, self.y = good_tiles[0][0], good_tiles[0][1]
            print('All good, pressing forwards.')
            return 1

        else:
            print('This was a mistake.')
            return 0


    def solve_fork(self, matrix, tiles, end):
        possibilities = []
        distances = []
        for new_x, new_y in tiles:
            distance = self.calculate_distance(new_x, new_y, *end)
            possibilities.append((new_x, new_y, distance))
            distances.append(distance)
        shortest_distance = min(distances)
        if shortest_distance < memory['distance']:
            for possibility in possibilities:
                if shortest_distance in possibility:
                    matrix[self.y][self.x] = 'm'
                    self.x, self.y, _ = possibility
                else:
                    print("I'd better remember these.")
                    memory['forks'].append(possibility)
            return 2
        else:
            print("I'd better turn around.")
            return 0

    
    def remember_fork(self, forks):
        try:
            distances = []
            for fork in forks:
                _, _, dist = fork
                distances.append(dist)
            min_distance = min(distances)
            for fork in forks:
                if min_distance in fork:
                    stop_x, stop_y, _ = fork
                    points['stop'] = (stop_x, stop_y)
        except ValueError:
            print("I think I'm stuck boss. Can you confirm?")
            input()
            sys.exit()


def check_y_axis(matrix, y, x, path):
    visible_y = []
    next_y = [y]
    while next_y != []:
        check_y = next_y.pop(-1) + path
        try:
            if matrix[check_y][x] == 1 and check_y >= 0:
                visible_y.append((x, check_y))
            elif matrix[check_y][x] in points['visible'] and check_y >= 0:
                next_y.append(check_y)
                visible_y.append((x, check_y))
                for new_x in range(x - 1, x + 2, 2):
                    try:
                        if matrix[check_y][new_x] == 1 and new_x >= 0:
                            visible_y.append((new_x, check_y))
                    except IndexError:
                        continue
        except IndexError:
            continue
    return visible_y
                
        
def check_x_axis(matrix, y, x, path):
    visible_x = []
    next_x = [x]
    while next_x != []:
        check_x = next_x.pop(-1) + path
        try:
            if matrix[y][check_x] == 1 and check_x >= 0:
                visible_x.append((check_x, y))
            elif matrix[y][check_x] in points['visible'] and check_x >= 0:
                next_x.append(check_x)
                visible_x.append((check_x, y))
                for new_y in range(y - 1, y + 2, 2):
                    try:
                        if matrix[new_y][check_x] == 1 and new_y >= 0:
                            visible_x.append((check_x, new_y))
                    except IndexError:
                        continue
        except IndexError:
            continue
    return visible_x 


def create_visible_matrix(matrix):
    for y, a in enumerate(matrix):
        for x, b in enumerate(a):
            if b == 'B' or b == 'F':
                continue
            else:
                matrix[y][x] = ' '


def clear():
    '''Function for clearing the cmd.'''
    os.system('cls')


def show_maze(matrix):
    '''Function for diplaying the maze.'''
    print(np.matrix(matrix))


while points['continue'] == 'y':
    maze = lab.Matrix(matrixes['size'][0], matrixes['size'][1])
    points['start'] = lab.coordinates['start']
    points['end'] = lab.coordinates['end']
    matrixes['hidden'] = maze.matrix
    matrixes['open'] = copy.deepcopy(matrixes['hidden'])
    Bot(matrixes['hidden'])
    matrixes['size'][0] += 2
    matrixes['size'][1] += 2