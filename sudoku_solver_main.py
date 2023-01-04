import cv2
import sys
import os
import time
from sudoku_extractor import extract_sudoku
from number_extractor import extract_numbers
from backtrack_sudoku_solution import sudoku_solver
import matplotlib.pyplot as plt

def output(s):
    sys.stdout.write(str(s))

def display_sudoku(sudoku):
    for i in range(9):
        for j in range(9):
            cell = sudoku[i][j]
            if cell ==0 or isinstance(cell, set):
                output('.')
            else:
                output(cell)
            if (j+1)%3==0 and j<8:
                output('|')
            if j!=8:
                output(' ')
        output('\n')
        if (i+1)%3==0 and i<8:
            output('- - - - +- - - - - +- - - - -\n')

def show_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    plt.show()
    return

def main(pth):
    image = extract_sudoku(pth)
    grid = extract_numbers(image)
    print("\nInput Sudoku:\n")
    display_sudoku(grid.tolist())
    sudoku_solution = sudoku_solver(grid)
    print("\nSolved Sudoku:\n")
    display_sudoku(sudoku_solution.tolist())

def sec_to_hms(seconds):
    seconds = seconds % (24*3600)
    hour = seconds//3600
    seconds%=3600
    minutes = seconds//60
    seconds%=60
    return "%d:%02d:%08d" % (hour, minutes, seconds) 

if __name__=='__main__':
    # IMG_PTH='images/this1.png'
    # main(pth=IMG_PTH)
    t1 = time.time()
    path = os.path.join('images', os.listdir('images')[0])
    main(pth = path)
    print("Time taken:", round(time.time() - t1), 2)
    # try:
    #     t1 = time.time()
    #     main(pth = sys.argv[1])
    #     print("Time taken:", round(time.time() - t1), 2)
    # except:
    #     print(f'usage: {__file__.split('/')[-1]} path')
    #     print('Error: Incorrect format')