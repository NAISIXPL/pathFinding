from asyncio import Queue

import networkx as nx
from matplotlib import pyplot as plt

alphabet = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S',
    19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}
reversed_alphabet = {u: v for v, u in alphabet.items()}
class Path:
    def __init__(self, grid, connections, start):
        self.visited = set()
        self.seen = 1
        self.start = start
        self.grid = grid
        self.connections = connections
        self.path = []
        #self.bfs()
        #self.dfs()
        #self.mts()
        #self.greedy()
        self.path_AtoB()

    def bfs(self):
        queue = Queue()
        queue.put_nowait((self.start.name, [self.start.name]))
        while not queue.empty():
            current, path = queue.get_nowait()
            if len(path) == self.grid.NUMBER_OF_CITIES and self.connections.get_conn(current, self.start.name):
                self.path = path + [self.start.name]
                print("Goal has been achieved: ", self.path)
                return
            for neighbor in self.connections.get_neighbors(current):
                if neighbor not in path:
                    queue.put_nowait((neighbor, path + [neighbor]))
        print("END: No path found that visits all cities")

    def dfs(self):
        stack = []
        stack.append((self.start.name, [self.start.name]))
        while stack:
            current, path = stack.pop()
            if len(path) == self.grid.NUMBER_OF_CITIES and self.connections.get_conn(current, self.start.name):
                self.path = path + [self.start.name]
                print("Goal has been achieved: ", self.path)
                return
            for neighbor in self.connections.get_neighbors(current):
                if neighbor not in path:
                    stack.append((neighbor, path + [neighbor]))
        print("END: No path found that visits all cities")

    def mts(self):
        max_number_of_roads = self.grid.NUMBER_OF_CITIES-1
        number_of_roads = 0
        graph_mst = nx.Graph()
        id_min_A = 0
        id_min_B = 0
        last_value = 0
        first = True
        while number_of_roads < max_number_of_roads:
            min_distance = 1000
            for i in range(self.grid.NUMBER_OF_CITIES):
                for j in range(i+1,self.grid.NUMBER_OF_CITIES):
                    if self.connections.distance[i, j] < min_distance and self.connections.connections[i,j]:
                        if i in self.visited and j in self.visited:
                            break
                        if first:
                            min_distance = self.connections.distance[i, j]
                            id_min_A = i
                            id_min_B = j
                        if i in self.visited or j in self.visited:
                            min_distance = self.connections.distance[i, j]
                            id_min_A = i
                            id_min_B = j
            first = False
            self.visited.add(id_min_A)
            self.visited.add(id_min_B)
            number_of_roads += 1
            self.connections.distance[id_min_A,id_min_B] = 1000
            print(f'Added road from {id_min_A} to {id_min_B}. MIN = {min_distance} | LAST = {last_value}')
            graph_mst.add_edge(id_min_A, id_min_B,weight=min_distance)
        nx.relabel_nodes(graph_mst,alphabet ,copy=False)
        nx.draw(graph_mst, with_labels=True)
        plt.show()

    def greedy(self):
        stack = []
        stack.append((self.start.name, [self.start.name]))
        while stack:
            current, path = stack.pop()
            if len(path) == self.grid.NUMBER_OF_CITIES and self.connections.get_conn(current, self.start.name):
                self.path = path + [self.start.name]
                print("Goal has been achieved: ", self.path)
                return
            temp_nbhd = []
            min_distance = 1000
            temp_min_nbhd = ''
            for neighbor in self.connections.get_neighbors(current):
                temp_nbhd.append(neighbor)
            for neighbor in temp_nbhd:
                if self.connections.distance[reversed_alphabet[neighbor], reversed_alphabet[current]] < min_distance:
                   if neighbor not in self.visited:
                       temp_min_nbhd = neighbor
                       min_distance = self.connections.distance[reversed_alphabet[neighbor], reversed_alphabet[current]]

            stack.append((temp_min_nbhd, path + [temp_min_nbhd]))
            self.visited.add(current)
        print("END: No path found that visits all cities")

    def path_AtoB(self):
        goal = input("Provide goal city : ")
        stack = []
        stack.append((self.start.name, [self.start.name]))
        while stack:
            current, path = stack.pop()
            if current == goal:
                self.path = path
                print("Goal has been achieved: ", self.path)
                return
            for neighbor in self.connections.get_neighbors(current):
                if neighbor not in path:
                    stack.append((neighbor, path + [neighbor]))
        print(f"END: No path found that connects {self.start} and {goal}")








