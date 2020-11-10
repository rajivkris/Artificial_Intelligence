from z3 import *

x, y, z = Reals('x y z')

solver = Solver()
solver.add(2 * x + 3 * y == 5)
solver.add(y + 3 * z > 3)
solver.add(x - 3 * z <= 10)
print("Constraint added")

solver.add(x > -5, x <  5)
solver.add(y > 0)

print(f'Check satisfiability of solver {solver.check()}')
print(f'Solver model is {solver.model()}')
