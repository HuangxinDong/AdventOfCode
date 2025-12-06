import os
import operator
from itertools import zip_longest

def solve_math_homework1(grid, operators):
    """
    Part1 old solution
    """
    ops_map = {'+': operator.add, '*': operator.mul, '-': operator.sub, '/': operator.floordiv}

    rows = len(grid)
    cols = len(grid[0])
    answer_sum = 0

    for i in range(cols):
        answer = grid[0][i]
        for j in range(1,rows):
            answer = ops_map[operators[i]](answer, grid[j][i])
        answer_sum += answer
    
    return answer_sum


def solve_math_homework2(grid, operators):
    ops_map = {'+': operator.add, '*': operator.mul, '-': operator.sub, '/': operator.floordiv}
    answer_sum = 0

    for nums, op in zip(grid, operators):
        answer = nums[0]
        for i in nums[1:]:
            answer = ops_map[op](i,answer)
        answer_sum += answer

    return answer_sum


def grid_conversion(grid):
    """
    for grid2
    """
    new_grid = []
    new_list = []
    for col in grid:
        num_str = ''.join(ch for ch in col if ch.isdigit())
        if num_str:
            new_list.append(int(num_str))
        else:
            new_grid.append(new_list)
            new_list = []
    if new_list:
        new_grid.append(new_list)
    return new_grid


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    # file_path = os.path.join(script_dir, 'example_input.txt')
    file_path = os.path.join(script_dir, 'input.txt')
    if os.path.exists(file_path):
        with open(file_path) as f:
            lines = f.read().splitlines()

            grid1 = [list(map(int, line.split())) for line in lines[:-1]]
            grid2 = [list(col) for col in zip_longest(*lines[:-1], fillvalue=' ')] # solution found online
            operators = lines[-1].split()
            
            grid1_new = [list(col) for col in zip(*grid1)]
            grid2_new = grid_conversion(grid2)
            # print("Part1: ",solve_math_homework1(grid1, operators))
            print("Part1: ",solve_math_homework2(grid1_new,operators))
            print("Part2: ",solve_math_homework2(grid2_new,operators))
    else:
        print("Input file not found.")
    

    