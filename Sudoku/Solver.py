#!/usr/bin/python

import numpy as np

num_solution = 0

def is_possible(grid,y,x,n):
    """ checking line """
    for i in range(0,9):
        if grid[y][i] == n:
            return False

    """ checking column"""
    for i in range(0,9):
        if grid[i][x] == n :
            return False
    
    """ checking square """
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

def solve_sudoku(grid):
    global num_solution
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if is_possible(grid,y,x,n):
                        grid[y][x] = n
                        solve_sudoku(grid)
                        grid[y][x] = 0
                return
    num_solution += 1
    print(f'\nSolution {num_solution}')
    print(np.matrix(grid))
    input(f'\nOther Possibility?')


