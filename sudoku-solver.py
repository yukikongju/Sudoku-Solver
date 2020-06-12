#!/usr/bin/python

import numpy as np
import os
import time
from random import randint
from os import system, name

num_solution = 0
max_cells_removed = 0

grid_one_sol = [[5,3,0,0,7,0,0,0,0],
                [6,0,0,1,9,5,0,0,0],
                [0,0,8,0,0,0,0,6,0],
                [8,0,0,0,6,0,0,0,3],
                [4,0,0,8,0,3,0,0,1],
                [7,0,0,0,2,0,0,0,6],
                [0,6,0,0,0,0,2,8,0],
                [0,0,0,4,1,9,0,0,5],
                [0,0,0,0,8,0,0,7,9]]

grid_more_sol = [[5,3,0,0,7,0,0,0,0],
                 [6,0,0,1,9,5,0,0,0],
                 [0,9,8,0,0,0,0,6,0],
                 [8,0,0,0,6,0,0,0,3],
                 [4,0,0,8,0,3,0,0,1],
                 [7,0,0,0,2,0,0,0,6],
                 [0,6,0,0,0,0,2,8,0],
                 [0,0,0,4,1,9,0,0,5],
                 [0,0,0,0,8,0,0,0,0]]

grid = [[1,2,3,4,5,6,7,8,9],
        [4,5,6,7,8,9,1,2,3],
        [7,8,9,1,2,3,4,5,6],
        [2,3,1,5,6,4,8,9,7],
        [5,6,4,8,9,7,2,3,1],
        [8,9,7,2,3,1,5,6,4],
        [3,1,2,6,4,5,9,7,8],
        [6,4,5,9,7,8,3,1,2],
        [9,7,8,3,1,2,6,4,5]]

""" Difficulty: Number of Cells removed """
dict_difficulty = {
    1: 19, # easy
    2: 28, # medium
    3: 37, # hard
    4: 46, # expert
    5: 55, # insane
    6: 64, # godlike
}

def generate_grid():
    """ TODO: generate grid """
    remove_cells()

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

def set_grid_difficulty():
    global max_cells_removed
    while True:
        try:
            difficulty = int(input('Choose a difficulty. Easy: 1 , Medium: 2,' \
                + 'Hard: 3, Expert: 4, Insane: 5, Godlike: 6 \n'))
            if difficulty in range(1,7):
                max_cells_removed = dict_difficulty.get(difficulty)       
                return 
        except:
            print("Please type a valid number.")

if __name__ == "__main__":
    set_grid_difficulty()
    generate_grid()
    print(f'\nSudoku Grid:\n {np.matrix(grid)}')
    solve_sudoku()





