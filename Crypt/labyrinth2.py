import random as ran
import numpy as np
import os

coordinates = {
    'free': [],
    'map': [],
    '2b': [],
    'tobuild': [],
    'start': [],
    'end': [],
    'pickaxe': []
}

class Matrix:
    '''The matrix that's going to work as the solvable area. x and y are the ranges of the area used.'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print('Loading 10%')
        self.matrix = []
        self.create_area()
        print('Loading 30%')
        self.create_start()
        print('Loading 70%')
        self.wall_breaker()
        print('Loading 90%')
        self.start_point(self.matrix)
        self.end_point(self.matrix, 3, 'F')
        self.end_point(self.matrix, 3, 'p')
        #self.clear


    def create_area(self):
        for i in range(self.y):
            self.matrix.append([])
            for n in range(self.x):
                self.matrix[i].append(0)
        for i in range(self.y):
            for n in range(self.x):
                coordinates['free'].append((n, i))


    def create_outer_walls(self):
        for y in range(0, len(self.matrix) - 1):
            self.matrix[y][0] = 1
            coordinates['free'].remove((0, y))
            self.matrix[y][len(self.matrix[0]) - 1] = 1
            coordinates['free'].remove((len(self.matrix[0]) - 1, y))
        for x in range(0, len(self.matrix[0])):
            self.matrix[0][x] = 1
            self.matrix[len(self.matrix) - 1][x] = 1
            if (x, 0) in coordinates['free']:
                coordinates['free'].remove((x, 0))
            if (x, len(self.matrix) - 1) in coordinates['free']:
                coordinates['free'].remove((x, len(self.matrix) - 1))


    def create_start(self):
        #self.clear
        #print(np.matrix(self.matrix))
        start_x, start_y = ran.choice(coordinates['free'])
        coordinates['free'] = []
        self.add_coordinates(start_x, start_y, 'free')
        for y in range(start_y - 1, start_y + 2):
            #self.clear
            if y < 0 or y >= self.y:
                    continue
            elif self.matrix[y][start_x] == 0:
                self.matrix[y][start_x] = 'm'
                self.add_coordinates(start_x, y, 'free')
                #print(np.matrix(self.matrix))
        for x in range(start_x - 1, start_x + 2):
            #self.clear
            if x < 0 or x >= self.x:
                    continue
            elif self.matrix[start_y][x] == 0:
                self.matrix[start_y][x] = 'm'
                self.add_coordinates(x, start_y, 'free')
                #print(np.matrix(self.matrix))
        for y in range(start_y - 1, start_y + 2):
            for x in range(start_x - 1, start_x + 2):
                #self.clear
                if x < 0 or x >= self.x or y < 0 or y >= self.y:
                    continue
                elif self.matrix[y][x] == 0:
                    self.matrix[y][x] = 1
                    #print(np.matrix(self.matrix))

        while coordinates['free'] != []:
            #print(np.matrix(self.matrix))
            next_x, next_y = coordinates['free'].pop(ran.randrange(0, len(coordinates['free'])))
            coordinates['2b'] = []
            for y in range(next_y - 1, next_y + 2, 2):
                self.add_coordinates(next_x, y, '2b')
            for x in range(next_x - 1, next_x + 2, 2):
                self.add_coordinates(x, next_y, '2b')
            for x, y in coordinates['2b']:
                self.check_tile(x, y)

            if coordinates['tobuild'] != []:  
                build = ran.choice(coordinates['tobuild'])
                coordinates['tobuild'].remove(build)
                coordinates['free'].append(build)
                self.matrix[build[1]][build[0]] = 'm'
                while coordinates['tobuild'] != []:
                    wall = coordinates['tobuild'].pop(-1)
                    self.matrix[wall[1]][wall[0]] = 1
            #self.clear
        
        #print(np.matrix(self.matrix))
        for y, a in enumerate(self.matrix):
            for x, b in enumerate(a):
                if self.matrix[y][x] == 0:
                    coordinates['free'].append((x, y))
        if coordinates['free'] != []:
            self.create_start()


    def check_tile(self, x, y):
        if x == self.x or x < 0 or y == self.y or y < 0:
            return
        elif self.matrix[y][x] == 'm' or self.matrix[y][x] == 1:
            return
        for test_y in range(y - 1, y + 2, 2):
            try:
                if self.matrix[test_y][x] == 'm':
                    continue
                else:
                    self.add_coordinates(x, y, 'tobuild')
            except IndexError:
                continue
        for test_x in range(x - 1, x + 2, 2):
            try:
                if self.matrix[y][test_x] == 'm':
                    continue
                else:
                    self.add_coordinates(x, y, 'tobuild')
            except IndexError:
                continue


    def add_coordinates(self, x, y, directory):
        if (x, y) not in coordinates[directory]:
            coordinates[directory].append((x, y))
        else:
            return
    

    def wall_breaker(self):
        ones = []
        for y, a in enumerate(self.matrix):
            for x, b in enumerate(a):
                if b == 1:
                    wall = 0
                    path = 0
                    try:
                        for nu_y in range(y - 1, y + 2, 2):
                            if self.matrix[nu_y][x] == 1:
                                wall += 1
                            elif self.matrix[nu_y][x] == 'm':
                                path += 1
                        if wall == 2:
                            path = 0
                            for nu_x in range(x - 1, x + 2, 2):
                                if self.matrix[y][nu_x] == 'm':
                                    path += 1
                                if path == 2:
                                    #self.clear
                                    self.matrix[y][x] = 'm'
                                    #print(np.matrix(self.matrix))
                        else:
                            wall = 0
                            for nu_x in range(x - 1, x + 2, 2):
                                if self.matrix[y][nu_x] == 1:
                                    wall += 1
                                if wall == 2:
                                    ##self.clear
                                    self.matrix[y][x] = 'm'
                                    ##print(np.matrix(self.matrix))
                    
                    except IndexError:
                        continue

    def clear(self):
        os.system('cls')

    def start_point(self, matrix):
        '''Function goes through the maze and randomizes a starting point from one of the edges. That's where the doors are.'''
        starting_coords = []
        for y, a in enumerate(matrix):
            for x, b in enumerate(a):
                if x == 0 or x == len(a) - 1 or y == 0 or y == len(matrix) - 1:
                    if b == 'm':
                        starting_coords.append((x, y))
        
        x, y = ran.choice(starting_coords)
        coordinates['start'] = (x, y)
        self.matrix[y][x] = 'S'


    def end_point(self, matrix, num_close_tiles, tile):
        '''Function searches for a possible endpoint to use as the winning condition. If a valid end point is found,
        it's marked in the matrixes. If no valid end point is found, the function restarts with a more lax valid condition.'''
        end_coords = []
        for y, a in enumerate(matrix):
            for x, b in enumerate(a):
                if b == 'm':
                    check = self.check_end_point(matrix, x, y, num_close_tiles)
                    if check == True:
                        end_coords.append((x, y))
        if end_coords != []:
            end_x, end_y = ran.choice(end_coords)
            end_coords.remove((end_x, end_y))
            if tile == 'F':
                coordinates['end'] = (end_x, end_y)
            elif tile == 'p':
                coordinates['pickaxe'] = (end_x, end_y)
            self.matrix[end_y][end_x] = tile
        else:
            self.end_point(matrix, num_close_tiles - 1, tile)


    def check_end_point(self, matrix, x, y, num_close_tiles):
        '''Function checks for a good endpoint to use. Returns true if the point is valid
        and return false if it's not.'''                
        num = 0
        for test_y in range(y - 1, y + 2, 2):
            try:
                if matrix[test_y][x] == 1:
                    num += 1
            except IndexError:
                continue
        for test_x in range(x - 1, x + 2, 2):
            try:
                if matrix[y][test_x] == 1:
                        num += 1
            except IndexError:
                continue
        if num == num_close_tiles:
            return True
        else:
            return False






if __name__ == "__main__":
    mt = Matrix(10, 10)
    print(np.matrix(mt.matrix))