from z3 import *

boxes = [[Int(str(i) + str(j)) for j in range(9)] for i in range(9)]
row_constraint = [Distinct([boxes[i][j] for j in range(9)]) for i in range(9)]
col_constraint = [Distinct([boxes[j][i] for j in range(9)]) for i in range(9)]
square_constraint1 = Distinct([boxes[i][j] for j in range(0, 3) for i in range(0, 3)])
square_constraint2 = Distinct([boxes[i][j] for j in range(3, 6) for i in range(3, 6)])
square_constraint3 = Distinct([boxes[i][j] for j in range(6, 9) for i in range(6, 9)])
val_constraint = [And(boxes[i][j] >= 1, boxes[i][j] <= 9) for j in range(9) for i in range(9)]

sudoku_solver = Solver()
sudoku_solver.add(row_constraint)
sudoku_solver.add(col_constraint)
sudoku_solver.add(square_constraint1)
sudoku_solver.add(square_constraint2)
sudoku_solver.add(square_constraint3)
sudoku_solver.add(val_constraint)

board = ((0, 0, 3, 0, 2, 0, 6, 0, 0),
         (9, 0, 0, 3, 0, 5, 0, 0, 1),
         (0, 0, 1, 8, 0, 6, 4, 0, 0),
         (0, 0, 8, 1, 0, 2, 9, 0, 0),
         (7, 0, 0, 0, 0, 0, 0, 0, 8),
         (0, 0, 6, 7, 0, 8, 2, 0, 0),
         (0, 0, 2, 6, 0, 9, 5, 0, 0),
         (8, 0, 0, 2, 0, 3, 0, 0, 9),
         (0, 0, 5, 0, 1, 0, 3, 0, 0))
        
sudoku_solver.add([If(board[i][j] == 0, True, boxes[i][j] == board[i][j]) for j in range(9) for i in range(9)])
assert sudoku_solver.check() == sat, "Uh oh. The solver didn't find a solution. Check your constraints."
for row, _boxes in enumerate(boxes):
    if row and row % 3 == 0:
        print('-'*9+"|"+'-'*9+"|"+'-'*9)
    for col, box in enumerate(_boxes):
        if col and col % 3 == 0:
            print('|', end='')
        print(' {} '.format(sudoku_solver.model()[box]), end='')
    print()