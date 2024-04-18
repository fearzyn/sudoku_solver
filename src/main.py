from solver.solver import Solver
import time

board = []
for num in range(1, 10):
    row = input("Enter row {}: ".format(num))
    temp = []
    for num in row:
        temp.append(int(num))
    board.append(temp)

sol = Solver()
solved = sol.solve(board)
time.sleep(3)
sol.automate(solved)