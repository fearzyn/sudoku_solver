import pyautogui as pg
import numpy as np
import time

board = []
for num in range(1,10):
    theInput = input("Enter row {}: ".format(num))
    tempList = []
    for num in theInput:
        tempList.append(int(num))
    board.append(tempList)

time.sleep(2)



# Sudoku helper function
def valid(row, col, number):
    for i in range(9):
        # Check row
        if board[row][i] == number:
            return False
        # Check column
        if board[i][col] == number:
            return False
    # Check 3x3 boxes
    corner_row = row - row % 3
    corner_col = col - col % 3
    for x in range(3):
        for y in range(3):
            if board[corner_row + x][corner_col + y] == number:
                return False
    # If number passes, then it must be a valid number to place
    return True


def Print(board):
    # Turns int board to string board
    final = []
    str_fin = []
    for i in range(9):
        final.append(board[i])

    for lists in final:
        for num in lists:
            str_fin.append(str(num))

    # pyautogui 
    counter = []
    for num in str_fin:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter) % 9 == 0:
            pg.hotkey('down')
            for i in range(9):
                pg.hotkey('left')
          


# Sudoku solver
def solve():
    global board
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if valid(row, col, num):
                        board[row][col] = num
                        solve()
                        board[row][col] = 0
                return
    Print(board)


solve()
