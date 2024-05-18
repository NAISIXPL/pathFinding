import numpy as np
import random

alphabet = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S',
    19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

NUMER_OF_CITIES = 3


class Grid:
    def __init__(self):
        self.cities = np.empty(NUMER_OF_CITIES, dtype=object)
        self.cities_cords = random.sample([(i, j) for i in range(-100, 101) for j in range(-100, 101)], NUMER_OF_CITIES)
        city_id = 0
        for i, city in enumerate(self.cities_cords):
            self.cities[i] = City(city[0], city[1], name_id=city_id)
            city_id += 1


class City:
    def __init__(self, x, y, name_id=-1):
        self.x = x
        self.y = y

        if name_id != -1:
            self.name = alphabet[name_id]
        else:
            self.name = ''


class Connections:
    def __init__(self, grid, percent_of_connections=1):
        self.connections = np.empty((NUMER_OF_CITIES, NUMER_OF_CITIES), dtype=object)
        for i in range(NUMER_OF_CITIES):
            for j in range(NUMER_OF_CITIES):
                city_1 = grid.cities[i]
                city_2 = grid.cities[j]
                distance = np.sqrt(np.power(city_1.x - city_2.x, 2) + np.power(city_1.y - city_2.y, 2))
                self.connections[i, j] = [1, distance]
        if percent_of_connections != 1:
            delete_percentage = 1 - percent_of_connections
            conn_to_delete = int((delete_percentage * NUMER_OF_CITIES ** 2) / 2)
            possible_pairs = [(i, j) for i in range(NUMER_OF_CITIES) for j in range(i + 1, NUMER_OF_CITIES)]
            pairs_to_delete = random.sample(possible_pairs, conn_to_delete)

            for i, j in pairs_to_delete:
                self.connections[i, j][0] = 0
                self.connections[j, i][0] = 0
