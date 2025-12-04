import os

def find_adjuscent(i, j, grid):
    """
    return the number of adjuscent @s
    """
    rolls = 0
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dr, dc in dirs:
        ni = i + dr
        nj = j + dc
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
            if grid[ni][nj] == "@":
                rolls += 1
        else:
            continue
    return rolls


def access_rolls(grid):
    """
    Find how many rolls of paper can be accessed by a forklift?
    """
    accessable_rolls = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "@":
                if find_adjuscent(i, j, grid) < 4:
                    accessable_rolls += 1
    return accessable_rolls


def remove_rolls(grid):
    removed_rolls = 0
    rows = len(grid)
    cols = len(grid[0])

    while access_rolls(grid):
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "@":
                    if find_adjuscent(i, j, grid) < 4:
                        removed_rolls += 1
                        grid[i][j] = "."
    return removed_rolls


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'input.txt')
    if os.path.exists(file_path):
        with open(file_path) as f:
            lines = f.read().splitlines()
            grid = []        
            for r in lines:
                grid.append(list(r))
        print(access_rolls(grid))
        print(remove_rolls(grid))
    else:
        print("Input file not found.")