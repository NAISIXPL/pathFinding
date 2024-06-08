import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt

alphabet = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S',
    19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

reversed_alphabet = {u: v for v, u in alphabet.items()}
NUMER_OF_CITIES = 5


class Grid:
    def __init__(self):
        self.NUMBER_OF_CITIES = NUMER_OF_CITIES
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
        self.connections = np.ones((NUMER_OF_CITIES, NUMER_OF_CITIES), dtype=int)
        np.fill_diagonal(self.connections, 0)

        self.distance = np.zeros((NUMER_OF_CITIES, NUMER_OF_CITIES), dtype=float)
        for i in range(NUMER_OF_CITIES):
            for j in range(NUMER_OF_CITIES):
                city_1 = grid.cities[i]
                city_2 = grid.cities[j]
                distance = np.sqrt(np.power(city_1.x - city_2.x, 2) + np.power(city_1.y - city_2.y, 2))
                distance = np.round(distance, 2)
                self.distance[i, j] = distance
        print(self.distance)
        if percent_of_connections != 1:
            delete_percentage = 1 - percent_of_connections
            conn_to_delete = int((delete_percentage * NUMER_OF_CITIES ** 2) / 2)
            possible_pairs = [(i, j) for i in range(NUMER_OF_CITIES) for j in range(i + 1, NUMER_OF_CITIES)]
            pairs_to_delete = random.sample(possible_pairs, conn_to_delete)

            for i, j in pairs_to_delete:
                self.connections[i, j] = 0
                self.connections[j, i] = 0

        self.graph = nx.from_numpy_array(self.connections)

        for i in range(NUMER_OF_CITIES):
            for j in range(i + 1, NUMER_OF_CITIES):
                if self.connections[i, j] == 1:
                    self.graph.add_edge(i, j, weight=self.distance[i, j])

        nx.relabel_nodes(self.graph, alphabet, copy=False)

        pos = nx.spring_layout(self.graph)  # Positions for all nodes
        nx.draw_circular(self.graph, with_labels=True, node_size=500, node_color='skyblue', font_size=10)

        # Draw edge labels (weights)
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        pos = nx.circular_layout(self.graph)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)

        plt.show()

    def get_neighbors(self, state):  # Returns list of neighbours
        id = reversed_alphabet[state]
        neighbours = []
        for i in range(NUMER_OF_CITIES):
            if self.connections[id, i] == 1:
                name = alphabet[i]
                neighbours.append(name)
        return neighbours

    def get_distance(self, A, B):
        id_A = reversed_alphabet[A]
        id_B = reversed_alphabet[B]
        return self.distance[id_A, id_B]

    def get_conn(self, A, B):
        id_A = reversed_alphabet[A]
        id_B = reversed_alphabet[B]
        return self.connections[id_A, id_B]
