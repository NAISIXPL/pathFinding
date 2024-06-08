from structure import Grid, Connections
from path_algorithm import Path

if __name__ == "__main__":
    grid = Grid()
    connections = Connections(grid,0.6)
    for city in grid.cities:
        print(f'City {city.name} is located at ({city.x, city.y})')

    print("Choose the starting city\n")
    start_city = input()
    for city in grid.cities:
        if city.name == start_city:
            start_city = city
    path = Path(grid, connections, start_city)
