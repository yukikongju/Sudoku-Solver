#!/usr/bin/python

import numpy as np
import os
import time
from os import system, name

from Sudoku.Solver import solve_sudoku
from Sudoku.Generator import generate_grid

if __name__ == "__main__":
    grid = generate_grid()
    print(f'\nSudoku Grid:\n {np.matrix(grid)}')
    solve_sudoku(grid)





