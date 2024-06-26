import os
import time

def load_grid(filename):
    """
    Load grid from file.

    Args:
        filename (str): Name of the file containing the grid.

    Returns:
        list: A 2D list representation of the grid with '0' replaced by ' '
              and '1' replaced by '*'.
    """
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            row = line.strip().replace('0', ' ').replace('1', '*')
            grid.append(list(row))
    return grid

def print_grid(grid):
    """
    Print the grid to the terminal.

    Args:
        grid (list): A 2D list representation of the grid.
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal screen
    for row in grid:
        print(' '.join(cell for cell in row))
    print("\n" + "-" * (len(grid[0]) * 2))

def step(grid):
    """
    Perform a single step in the game of life simulation.

    Args:
        grid (list): A 2D list representation of the grid.

    Returns:
        list: A 2D list representation of the updated grid.
    """
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
    """
    Count the number of live neighbors for a given cell.

    Args:
        grid (list): A 2D list representation of the grid.
        x (int): x-coordinate of the cell.
        y (int): y-coordinate of the cell.

    Returns:
        int: The number of live neighbors.
    """
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
    """
    Start the game of life simulation.

    Args:
        grid (list): A 2D list representation of the grid.
        delay (float, optional): Delay between steps in seconds. Defaults to 0.5.
    """
    while True:
        print_grid(grid)
        grid = step(grid)
        time.sleep(delay)
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal screen

def main():
    """
    Main function to run the game of life simulation.
    """
    filename = input("Enter the filename with the grid (should contain 0s and 1s): ").strip()
    grid = load_grid(filename)
    start_simulation(grid)

if __name__ == "__main__":
    main()
