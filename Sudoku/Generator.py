#!/usr/bin/python

import numpy as np
from random import randint
from Sudoku.Solver import is_possible

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

empty_grid = np.zeros([9,9], dtype = int)

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
    set_grid_difficulty()

    """ TODO: solution grid """
    
    remove_cells()
    return grid

def generate_one_sol_grid():
    pass

def generate_multiple_sol_grid():
    pass                 

def remove_cells():
    num_cells_removed = 0
    while num_cells_removed < max_cells_removed:
        x = randint(0,8) # grid index range from 0 and 8
        y = randint(0,8)
        if grid[y][x] != 0:
            grid[y][x] = 0
            num_cells_removed += 1

def set_grid_difficulty():
    global max_cells_removed
    while True:
        try:
            difficulty = int(input('Choose a difficulty. Easy: 1, Medium: 2, ' \
                + 'Hard: 3, Expert: 4, Insane: 5, Godlike: 6 \n'))
            if difficulty in range(1,7):
                max_cells_removed = dict_difficulty.get(difficulty)       
                return 
        except:
            print("Please type a valid number.")


