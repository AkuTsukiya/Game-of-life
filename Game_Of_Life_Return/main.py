import numpy as np
from time import sleep


def grid_initialisation(AlivePercent , row, col):
    grid = [[0 for _ in range(col)] for _ in range(row)]

    for i in range(row):
        for j in range(col):
            if np.random.randint(0 , 101) <= AlivePercent:
                grid[i][j] = 1
    return grid

def show_grid(grid):
    for item in grid:
        for iitem in item:
            iitem = "\u2588" if iitem == 1 else " "
            print(iitem, end="")
        print("")
    print("-----------------------------------------")

def count_neightbor(grid , x , y , row , col):
    active_cell = 0
    if grid[x][y]==1:
        active_cell = -1
    for i in range(-1 , 2):
        for j in range(-1 , 2):
            if ((x+i) >= 0 and (y+j) >= 0) and ((x+i)<row and (y+j)< col): 
                active_cell += grid[x+i][y+j]
    return active_cell

def next_generation(grid , row , col):
    new_grid = [[0 for _ in range(col)] for _ in range(row)]
    for x in range(row):
        for y in range(col):
            neightbor = count_neightbor(grid , x , y , row , col)
            if neightbor == 3 or (neightbor ==2 and grid[x][y] == 1) :
                new_grid[x][y] = 1
            else:
                new_grid[x][y]=0
    return new_grid







def main():

    print("What is the '%' of cell alive ?")
    AlivePercent = int(input())

    print("Number of row ?")
    row = int(input())

    print("Number of col ?")
    col = int(input())

    print("Number of generation ? (93 for infinite generation)")
    NoG = int(input())



    grid = grid_initialisation(AlivePercent, row, col)
    show_grid(grid)


    if NoG == 93:
        while True:
            grid = next_generation(grid , row , col)
            show_grid(grid)
            sleep(2)
    else:
        for i in range(NoG):
            grid = next_generation(grid , row , col)
            show_grid(grid)
            sleep(2)

    
