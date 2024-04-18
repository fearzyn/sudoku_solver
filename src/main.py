from solver.solver import Solver
import time

board = []
print("Enter 0 for empty cells. Be prepared to click the top left corner of the board.")
for num in range(1, 10):
    while True:
        row = input("Enter row {}: ".format(num))
        if len(row) == 9:
            break
        print("Invalid row. Please try again.")

    temp = []
    for num in row:
        temp.append(int(num))
    board.append(temp)

sol = Solver()
solved = sol.solve(board)

print("Preparing to solve in 3 seconds. Click the top left corner of the board.")
time.sleep(1)
print("3")

time.sleep(1)
print("2")

time.sleep(1)
print("1")

sol.automate(solved)
print("Solved!")