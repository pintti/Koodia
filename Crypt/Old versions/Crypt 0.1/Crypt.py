import labyrinth2 as lab
import random as ran
import numpy as np
import os
from msvcrt import getch
import copy
import sys


matrixes = {
    'size': [10, 10],
    'open': [],
    'hidden': []
}

moves = {
    'axis': {
        'y': [72, 80],
        'x': [77, 75]
    },
    72: -1,
    77: 1,
    80: 1,
    75: -1,
}

points = {
    'end': [],
    'continue': 'y',
    'visible': ['F', 'm', 'S']
}

class Bot():
    '''This lil fella is going to be running through a labyrinth trying to solve it. Godspeed lil bot, godspeed.'''
    def __init__(self, matrix):
        pass


class Player():
    '''This is you. I made this for fun, just to see if it was hard to make a controlled entity to run in the labyrinth.'''
    def __init__(self, matrix):
        print(np.matrix(matrix))
        start_x, start_y = start_point(matrix)
        matrixes['hidden'][start_y][start_x] = 'S'
        self.x = start_x
        self.y = start_y
        end_point(matrixes['hidden'], 3)
        self.main_player(matrix)


    def main_player(self, matrix):
        '''This is the main function for the player. It loops around until a win condition is reached.'''
        while (self.x, self.y) != points['end']:
            self.movement(matrix)
        clear()
        matrix[self.y][self.x] = 'P'
        show_maze(matrix)
        print('Want to delve deeper? (Y/N)')
        while True:
            ans = self.get_key()
            if ans == 121:
                points['continue'] = 'y'
                return
            elif ans == 110 or ans == 27:
                points['continue'] = 'n'
                return
            else:
                continue


    def movement(self, matrix):
        '''Code for the movement of the player. x and y are the points where the player is.'''
        matrix[self.y][self.x] = 'P'
        create_visible_matrix(matrix)
        self.check_vision(matrixes['hidden'])
        clear()
        show_maze(matrix)
        key = self.get_key()
        self.check_move(matrix, key)


    def get_key(self):
        '''Function checks which key was pressed. Thanks to how getch and arrow keys work, the getch function needs 
        to be ran twice for the proper value to appear. 27 is ESC and can be identified instantly.'''
        key = ord(getch())
        if key != 224:
            return key
        key = ord(getch())
        return key

    
    def check_move(self, matrix, key):
        '''Function checks whether or not the players move is valid. If the player tries to walk into a wall, the function doesn't
        let them. Same with trying to walk OOB. If the player pressed ESC button, the funtion shuts everything down.'''
        if key in moves['axis']['y']:
            new_y = self.y + moves[key]
            if new_y < 0 or new_y >= len(matrix):
                return
            elif matrixes['hidden'][new_y][self.x] == 1:
                return
            else:
                matrix[self.y][self.x] = matrixes['hidden'][self.y][self.x]
                self.y = new_y
        elif key in moves['axis']['x']:
            new_x = self.x + moves[key]
            if new_x < 0 or new_x >= len(matrix[0]):
                return
            elif matrixes['hidden'][self.y][new_x] == 1:
                return
            else:
                matrix[self.y][self.x] = matrixes['hidden'][self.y][self.x]
                self.x = new_x
        elif key == 27:
            sys.exit()
        

    def check_vision(self, matrix):
        '''Function checks the players cone of vision and shows him what he should be able to see.'''
        visible = []
        visible.append(check_y_axis(matrix, self.y, self.x, 1))
        visible.append(check_y_axis(matrix, self.y, self.x, -1))
        visible.append(check_x_axis(matrix, self.y, self.x, 1))
        visible.append(check_x_axis(matrix, self.y, self.x, -1))
        
        for visibles in visible:
            for x, y in visibles:
                try:
                    if matrixes['open'][y][x] == ' ':
                        matrixes['open'][y][x] = matrixes['hidden'][y][x]
                except IndexError:
                    continue
        

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
            if b == 'P':
                continue
            elif b == 'F':
                continue
            else:
                matrix[y][x] = ' '


def start_point(matrix):
    '''Function goes through the maze and randomizes a starting point from one of the edges. That's where the doors are.'''
    starting_coords = []
    for y, a in enumerate(matrix):
        for x, b in enumerate(a):
            if x == 0 or x == len(a) - 1 or y == 0 or y == len(matrix) - 1:
                if b == 'm':
                    starting_coords.append((x, y))
    
    x, y = ran.choice(starting_coords)
    return x, y


def end_point(matrix, num_close_tiles):
    '''Function searches for a possible endpoint to use as the winning condition. If a valid end point is found,
    it's marked in the matrixes. If no valid end point is found, the function restarts with a more lax valid condition.'''
    end_coords = []
    for y, a in enumerate(matrix):
        for x, b in enumerate(a):
            if b == 'm':
                check = check_end_point(matrix, x, y, num_close_tiles)
                if check == True:
                    end_coords.append((x, y))
    if end_coords != []:
        end_x, end_y = ran.choice(end_coords)
        points['end'] = (end_x, end_y)
        matrixes['open'][end_y][end_x] = 'F'
        matrixes['hidden'][end_y][end_x] = 'F'
    else:
        end_point(matrix, num_close_tiles - 1)


def check_end_point(matrix, x, y, num_close_tiles):
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


def clear():
    '''Function for clearing the cmd.'''
    os.system('cls')


def show_maze(matrix):
    '''Function for diplaying the maze.'''
    print(np.matrix(matrix))


print('The amulet guides you. Delve deep and find the treasure. With the amulet and a torch in hand you descend down into the')
print('')
print('THE CRYPT')
print('')
print('Arrow keys to move. Press ESC at any time to quit. Press enter to descend.')
input()

while points['continue'] == 'y':
    maze = lab.Matrix(matrixes['size'][0], matrixes['size'][1])
    matrixes['hidden'] = maze.matrix
    matrixes['open'] = copy.deepcopy(matrixes['hidden'])
    Player(matrixes['open'])
    matrixes['size'][0] += 2
    matrixes['size'][1] += 2


#maze = lab.Matrix(matrixes['size'][0], matrixes['size'][1])
#matrixes['hidden'] = maze.matrix
#matrixes['open'] = copy.deepcopy(matrixes['hidden'])
#matrixes['open'][2][2] = 'P'
#print(np.matrix(matrixes['open']))
#create_visible_matrix(matrixes['open'])
#print(np.matrix(matrixes['open']))
