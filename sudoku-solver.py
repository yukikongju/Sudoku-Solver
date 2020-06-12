#!/usr/bin/python

import numpy as np
import os
import time
from random import randint
from os import system, name

num_solution = 0
max_cells_removed = 32

grid_one_sol = [[5,3,0,0,7,0,0,0,0],
                [6,0,0,1,9,5,0,0,0],
                [0,0,8,0,0,0,0,6,0],
                [8,0,0,0,6,0,0,0,3],
                [4,0,0,8,0,3,0,0,1],
                [7,0,0,0,2,0,0,0,6],
                [0,6,0,0,0,0,2,8,0],
                [0,0,0,4,1,9,0,0,5],
                [0,0,0,0,8,0,0,7,9]]

grid = [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,0,0]]


def remove_cells():
    num_cells_removed = 0
    while num_cells_removed < max_cells_removed:
        x = randint(0,8) # grid index range from 0 and 8
        y = randint(0,8)
        if grid[y][x] != 0:
            grid[y][x] = 0
            num_cells_removed += 1

def is_possible(y,x,n):
    global grid
    
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

def solve_sudoku():
    global grid
    global num_solution
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if is_possible(y,x,n):
                        grid[y][x] = n
                        solve_sudoku()
                        grid[y][x] = 0
                return
    num_solution += 1
    print(f'\nSolution {num_solution}')
    print(np.matrix(grid))
    input(f'\nOther Possibility?')

if __name__ == "__main__":
    print(f'\nSudoku Grid:\n {np.matrix(grid)}')
    solve_sudoku()




