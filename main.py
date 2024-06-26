import os
import time

def load_grid(filename):
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            row = line.strip().replace('0', ' ').replace('1', '*')
            grid.append(list(row))
    return grid

def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal screen
    for row in grid:
        print(' '.join(cell for cell in row))
    print("\n" + "-" * (len(grid[0]) * 2))

def step(grid):
    new_grid = [[' '] * len(grid[0]) for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            live_neighbors = count_live_neighbors(grid, i, j)
            if grid[i][j] == '*':
                new_grid[i][j] = '*' if live_neighbors in [2, 3] else ' '
            else:
                new_grid[i][j] = '*' if live_neighbors == 3 else ' '
    return new_grid

def count_live_neighbors(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            count += 1 if grid[nx][ny] == '*' else 0
    return count

def start_simulation(grid, delay=0.5):
    while True:
        print_grid(grid)
        grid = step(grid)
        time.sleep(delay)
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal screen

def main():
    filename = input("Enter the filename with the grid (should contain 0s and 1s): ").strip()
    grid = load_grid(filename)
    start_simulation(grid)

if __name__ == "__main__":
    main()
