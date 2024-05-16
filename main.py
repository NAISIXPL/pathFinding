import numpy as np
import random

alphabet = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S',
    19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'
}


class Grid:
    def __init__(self, up, left, down, right):
        self.upper_bound = up
        self.left_bound = left
        self.bottom_bound = down
        self.right_bound = right
        self.points = np.empty((200, 200), dtype=object)
        self.cities = random.sample([(i, j) for i in range(-100, 101) for j in range(-100, 101)], 26)
        city_id = 0
        for i in range(-100, 101):
            for j in range(-100, 101):
                if (i, j) in self.cities:
                    self.points[i, j] = Point(i, j, self.upper_bound, self.left_bound, self.bottom_bound,
                                              self.right_bound, id=city_id)
                    city_id += 1
                else:
                    self.points[i, j] = Point(i, j, self.upper_bound, self.left_bound, self.bottom_bound,
                                              self.right_bound)


class Point:
    def __init__(self, x, y, upper_bound, left_bound, bottom_bound, right_bound, id=-1):
        self.x = x
        self.y = y

        if id != -1:
            self.name = alphabet[id]
        else:
            self.name = ''
        if y == upper_bound and x == left_bound:
            self.north = False
            self.west = False
        if x == left_bound and y == bottom_bound:
            self.west = False
            self.south = False
        if y == bottom_bound and x == right_bound:
            self.south = False
            self.east = False
        if y == upper_bound and x == right_bound:
            self.north = False
            self.east = False
        elif y == upper_bound:
            self.north = False
        elif x == left_bound:
            self.west = False
        elif y == bottom_bound:
            self.south = False
        elif x == right_bound:
            self.east = False
        else:
            self.north = True
            self.west = True
            self.south = True
            self.east = True


class Path:
    def __init__(self, grid, start, end):
        pass


Grid(100, -100, -100, 100)
