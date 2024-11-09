import math
from time import sleep
import keyboard as kb


# СДЕЛАТЬ ЗАЛИВКУ РАЗЛИЧНЫМ ФИГУРАМ

class Grid:
    def __init__(self):
        self.grid = []

    def fill(self, win_x: int, win_y: int, char: str = ' '):
        """Creating and/or filling grid with 1 symbol"""
        self.grid = []
        for y in range(win_y+1):
            self.grid.append([])
            for x in range(win_x-1):
                self.grid[y].append(char)

    def print(self):
        """Printing lines of grid[] in console"""
        a = ''
        for y in range(len(self.grid)):
            a += '\n'
            for x in range(len(self.grid[0])):
                a += self.grid[y][x]
        print(a, end='')

    # def dot(self, dot_x, dot_y):
    #     """U dont ned it"""
    #     return dot_x, dot_y

    def dot(self, dot_, char: str = 'D'):
        """just like grid[x][y] = 'char', but in func"""
        try:
            self.grid[dot_[1]][dot_[0]] = char
        except (Exception,):
            pass

    def polygon_dot(self, rotation, rot_slide, radius, offset_x, offset_y):
        """Creating the dot, using centerXY, offset from center, rotation around center"""
        exit_y = round(math.cos(math.radians(-rotation + rot_slide)) * radius + offset_y)
        exit_x = math.sin(math.radians(-rotation + rot_slide)) * radius
        exit_x *= ((len(self.grid[0]) - 1) / (len(self.grid) - 1)) * (11 / 24)
        exit_x = round(exit_x + offset_x)

        return exit_x, exit_y

    def line(self, dot1, dot2, char: str = 'l'):
        """Filling grid with symbols from dot1 to dot2"""
        x1 = dot1[0]
        y1 = dot1[1]
        x2 = dot2[0]
        y2 = dot2[1]
        step = max(abs(y2 - y1), abs(x2 - x1))
        dx = (x2 - x1) / step
        dy = (y2 - y1) / step
        nx = x1
        ny = y1

        try:
            self.grid[y1][x1] = char
        except (Exception,):
            pass

        for i in range(1, step):
            try:
                self.grid[round(ny + dy)][round(nx + dx)] = char
            except (Exception,):
                pass
            nx += dx
            ny += dy
            try:
                self.grid[y2][x2] = char
            except (Exception,):
                pass

    def circle(self, center_x, center_y, radiusx, radiusy, char: str = 'C'):
        for i in range(360):
            exit_y = round(math.cos(math.radians(-i)) * radiusy + center_y)
            exit_x = math.sin(math.radians(-i)) * radiusx
            exit_x *= ((len(self.grid[0])) / (len(self.grid))) * (11 / 24)
            exit_x = round(exit_x + center_x)
            try:
                self.grid[exit_y][exit_x] = char
            except (Exception,):
                pass

    def text(self, pos_x, pos_y, text: str, vertical = False):
        try:
            if vertical:
                for i in range(len(text)):
                    self.grid[pos_y+i][pos_x] = text[i]
            else:
                for i in range(len(text)):
                    self.grid[pos_y][pos_x+i] = text[i]
        except (Exception,):
            pass

    def square(self, pos_x, pos_y, size_x, size_y, char = '#', fill = False):
        if not fill:
            try:
                for i in range(size_x):
                    self.grid[pos_y][pos_x+i] = char
                    self.grid[pos_y+size_y-1][pos_x+i] = char
                for i in range(size_y):
                    self.grid[pos_y+i][pos_x] = char
                    self.grid[pos_y+i][pos_x+size_x-1] = char

            except (Exception,):
                pass
        else:
            try:
                for y in range(size_y):
                    for x in range(size_x):
                        self.grid[pos_y+y][pos_x+x] = char

            except (Exception,):
                pass

    def save(self, filename):
        a = ''
        for y in range(len(self.grid)):
            if not y == 0:
                a += '\n'
            for x in range(len(self.grid[0])):
                a += self.grid[y][x]
        with open(filename, 'w') as f:
            f.write(a)

    def load(self, filename):

        self.grid = [[]]
        with open(filename, 'r') as f:
            saved = f.read()
            column = 0
            for i in range(len(saved)):
                if saved[i] == '\n':
                    self.grid.append([])
                    column += 1
                else:
                    self.grid[column].append(saved[i])
