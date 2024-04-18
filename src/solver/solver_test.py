import pytest
import copy # To not pass by reference
from solver import Solver, flatten

sol = Solver()

# Unsolved board
board1 = [[0, 0, 0, 4, 0, 0, 1, 9, 0], 
        [0, 3, 0, 0, 0, 0, 8, 6, 0], 
        [0, 0, 7, 0, 8, 3, 5, 0, 0], 
        [0, 0, 0, 0, 0, 8, 6, 0, 0], 
        [8, 0, 5, 1, 0, 0, 0, 0, 0], 
        [0, 2, 0, 0, 0, 0, 3, 5, 0], 
        [0, 8, 1, 0, 4, 0, 0, 0, 0], 
        [0, 0, 0, 0, 7, 0, 0, 0, 0], 
        [0, 4, 0, 2, 5, 0, 0, 0, 0]]

# Solved board
board2 = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]]          

def test_isValid():
    assert sol.isValid(0, 0, 1, copy.deepcopy(board1)) is False
    assert sol.isValid(0, 0, 6, copy.deepcopy(board1)) is True
    assert sol.isValid(0, 0, 9, copy.deepcopy(board1)) is False
    assert sol.isValid(0, 0, 4, copy.deepcopy(board1)) is False
    assert sol.isValid(7, 7, 5, copy.deepcopy(board1)) is False

    assert sol.isValid(0, 0, 5, copy.deepcopy(board2)) is False
    assert sol.isValid(0, 0, 6, copy.deepcopy(board2)) is False
    assert sol.isValid(8, 8, 9, copy.deepcopy(board2)) is False
    assert sol.isValid(100, 100, 9, copy.deepcopy(board2)) is False # out of bounds


def test_solve():
    assert sol.solve(copy.deepcopy(board1)) == [[6, 5, 8, 4, 2, 7, 1, 9, 3], 
                                                [4, 3, 2, 9, 1, 5, 8, 6, 7], 
                                                [9, 1, 7, 6, 8, 3, 5, 2, 4], 
                                                [3, 7, 4, 5, 9, 8, 6, 1, 2], 
                                                [8, 6, 5, 1, 3, 2, 7, 4, 9], 
                                                [1, 2, 9, 7, 6, 4, 3, 5, 8], 
                                                [5, 8, 1, 3, 4, 9, 2, 7, 6], 
                                                [2, 9, 6, 8, 7, 1, 4, 3, 5], 
                                                [7, 4, 3, 2, 5, 6, 9, 8, 1]]
    assert sol.solve(copy.deepcopy(board2)) is True # already solved

def test_flatten():
    assert flatten(copy.deepcopy(board1)) == ['0', '0', '0', '4', '0', '0', '1', '9', '0', 
                                            '0', '3', '0', '0', '0', '0', '8', '6', '0', 
                                            '0', '0', '7', '0', '8', '3', '5', '0', '0', 
                                            '0', '0', '0', '0', '0', '8', '6', '0', '0', 
                                            '8', '0', '5', '1', '0', '0', '0', '0', '0', 
                                            '0', '2', '0', '0', '0', '0', '3', '5', '0', 
                                            '0', '8', '1', '0', '4', '0', '0', '0', '0', 
                                            '0', '0', '0', '0', '7', '0', '0', '0', '0', 
                                            '0', '4', '0', '2', '5', '0', '0', '0', '0']
    
    assert flatten(copy.deepcopy(board2)) == ['5', '3', '4', '6', '7', '8', '9', '1', '2',
                                            '6', '7', '2', '1', '9', '5', '3', '4', '8',
                                            '1', '9', '8', '3', '4', '2', '5', '6', '7',
                                            '8', '5', '9', '7', '6', '1', '4', '2', '3',
                                            '4', '2', '6', '8', '5', '3', '7', '9', '1',
                                            '7', '1', '3', '9', '2', '4', '8', '5', '6',
                                            '9', '6', '1', '5', '3', '7', '2', '8', '4',
                                            '2', '8', '7', '4', '1', '9', '6', '3', '5',
                                            '3', '4', '5', '2', '8', '6', '1', '7', '9']

if __name__ == "__main__":
    pytest.main()