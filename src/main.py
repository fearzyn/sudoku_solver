from solver import Solver
import time

board = []
for num in range(1, 10):
    row = input("Enter row {}: ".format(num))
    temp = []
    for num in row:
        temp.append(int(num))
    board.append(temp)

time.sleep(3)

sol = Solver(board)
sol.solve()