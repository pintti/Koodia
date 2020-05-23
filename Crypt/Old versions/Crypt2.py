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
    'visible': ['F', 'm', 'S', 'p'],
    'pickaxe': 0,
    'pickedup': 0
}  


class Player():
    '''This is you. I made this for fun, just to see if it was hard to make a controlled entity to run in the labyrinth.'''
    def __init__(self, matrix, start_x, start_y):
        print(np.matrix(matrix))
        #start_x, start_y = start_point(matrix)
        #matrixes['hidden'][start_y][start_x] = 'S'
        self.x = start_x
        self.y = start_y
        #end_point(matrixes['hidden'], 3)
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
        self.check_vision(matrixes['hidden'], self.x, self.y)
        clear()
        show_maze(matrix)
        if matrixes['hidden'][self.y][self.x] == 'p':
            self.pick_up_pickaxe(matrix)
            matrixes['hidden'][self.y][self.x] = 'm'
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
                if points['pickaxe'] == 1:
                    matrixes['hidden'][new_y][self.x] = 'm'
                    points['pickaxe'] = 0
                else:
                    return
            else:
                matrix[self.y][self.x] = matrixes['hidden'][self.y][self.x]
                self.y = new_y
        elif key in moves['axis']['x']:
            new_x = self.x + moves[key]
            if new_x < 0 or new_x >= len(matrix[0]):
                return
            elif matrixes['hidden'][self.y][new_x] == 1:
                if points['pickaxe'] == 1:
                    matrixes['hidden'][self.y][new_x] = 'm'
                    points['pickaxe'] = 0
                else:
                    return
            else:
                matrix[self.y][self.x] = matrixes['hidden'][self.y][self.x]
                self.x = new_x
        elif key == 27:
            sys.exit()
        elif key == 112:
            #self.peek(matrix)
            print("Peeking needs to be reworked so it isn't currently available.")
        

    def check_vision(self, matrix, x, y):
        '''Function checks the players cone of vision and shows him what he should be able to see.'''
        visible = []
        visible.append(check_y_axis(matrix, y, x, 1))
        visible.append(check_y_axis(matrix, y, x, -1))
        visible.append(check_x_axis(matrix, y, x, 1))
        visible.append(check_x_axis(matrix, y, x, -1))
        for diag_y in range(y - 1, y + 2, 2):
            for diag_x in range(x - 1, x + 2, 2):
                if diag_y >= 0 and diag_x >= 0:
                    try:
                        if matrix[diag_y][diag_x] == 1:
                            continue
                        else:
                            diag = self.check_diag_vision(matrix, diag_x, diag_y, x, y)
                            if diag != None:
                                visible.append(diag)
                    except IndexError:
                        continue
                
        for visibles in visible:
            for x, y in visibles:
                try:
                    if matrixes['open'][y][x] == ' ':
                        matrixes['open'][y][x] = matrixes['hidden'][y][x]
                except IndexError:
                    continue

        
    def check_diag_vision(self, matrix, dx, dy, px, py):
        diag_visible = []
        walls = 0
        try:
            if matrix[dy][px] == 1:
                walls += 1
            if matrix[py][dx] == 1:
                walls += 1
            if walls == 2:
                return
            elif walls == 1:
                diag_visible.append((dx, dy))
                for y in range(dy - 1, dy + 2, 2):
                    if matrix[y][dx] == 1 and matrixes['size'][1] > y >= 0:
                        diag_visible.append((dx, y))
                for x in range(dx - 1, dx + 2, 2):
                    if matrix[dy][x] == 1 and matrixes['size'][0] > x >= 0:
                        diag_visible.append((x, dy))
                return diag_visible
            elif walls == 0:
                diag_visible.append((dx, dy))
                for y in range(dy - 1, dy + 2, 2):
                    if matrixes['size'][1] > y >= 0:
                        diag_visible.append((dx, y))
                for x in range(dx - 1, dx + 2, 2):
                    if matrixes['size'][0] > x >= 0:
                        diag_visible.append((x, dy))
                return diag_visible
                    
        except IndexError:
            return
                

    def pick_up_pickaxe(self, matrix):
        print('You have found a pickaxe! It can be used to break down one wall.')
        print('Press enter to continue.')
        points['pickedup'] = 0
        while points['pickedup'] == 0:
            key = ord(getch())
            if key == 13:
                points['pickedup'] = 1
        points['pickaxe'] = 1

    
    def peek(self, matrix):
        create_visible_matrix(matrix)
        peek_coords = []
        for y in range(self.y - 1, self.y + 2, 2):
            try:
                if matrixes['hidden'][y][self.x] == 'm':
                    peek_coords.append((y, self.x))
            except IndexError:
                continue
        for x in range(self.x - 1, self.x + 2, 2):
            try:
                if matrixes['hidden'][self.y][x] == 'm':
                    peek_coords.append((self.y, x))
            except IndexError:
                continue
        for y, x in peek_coords:
            self.check_vision(matrixes['hidden'], x, y)
            matrixes['open'][y][x] = matrixes['hidden'][y][x]
        clear()
        show_maze(matrix)
        getch()
      

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


def clear():
    '''Function for clearing the cmd.'''
    os.system('cls')


def show_maze(matrix):
    '''Function for diplaying the maze.'''
    print(np.matrix(matrix))

clear()
print('The amulet guides you. Delve deep and find the treasure. With the amulet and a torch in hand you descend down into the')
print('')
print('THE CRYPT')
print('')
print('Arrow keys to move. Press ESC at any time to quit. Press enter to descend.')
input()

while points['continue'] == 'y':
    maze = lab.Matrix(matrixes['size'][0], matrixes['size'][1])
    start_x, start_y = lab.coordinates['start'][0], lab.coordinates['start'][1]
    print(lab.coordinates['end'])
    points['end'] = lab.coordinates['end'][0], lab.coordinates['end'][1]
    matrixes['hidden'] = maze.matrix
    matrixes['open'] = copy.deepcopy(matrixes['hidden'])
    Player(matrixes['open'], start_x, start_y)
    matrixes['size'][0] += 2
    matrixes['size'][1] += 2



