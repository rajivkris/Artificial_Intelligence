from z3 import *

F, O, U, R, T, W,  = Ints('F O U R T W')  # create an z3.Int type variable instance called "F"

ca_solver = Solver()  # create an instance of a Z3 CSP solver

ca_solver.add(F >= 0, F <= 9, O >= 0, O <= 9, U >= 0, U <= 9, R >= 0, R <= 9, T >= 0, T <= 9, W >=0, W <= 9)  # add constraints to the solver: 0 <= F <= 9

ca_solver.add(F != 0, T != 0)

# TODO: Add a Distinct constraint for all the variables
ca_solver.add(F != O, F != U, F != R, F != T, F!= W, U != O, U != R, U != T, U != W, O != R, O != T, O != W, R != T, R != W, T != W)


# TODO: add any required variables and/or constraints to solve the cryptarithmetic puzzle
# Primary solution using single constraint for the cryptarithmetic equation
TWO = T * 10**2 + W * 10**1 + O
FOUR = F * 10**3 + O * 10**2 + U * 10**1 + R
ca_solver.add(TWO + TWO == FOUR)
assert ca_solver.check() == sat, "Uh oh...the solver did not find a solution. Check your constraints."
print("  T W O  :    {} {} {}".format(ca_solver.model()[T], ca_solver.model()[W], ca_solver.model()[O]))
print("+ T W O  :  + {} {} {}".format(ca_solver.model()[T], ca_solver.model()[W], ca_solver.model()[O]))
print("-------  :  -------")
print("F O U R  :  {} {} {} {}".format(ca_solver.model()[F], ca_solver.model()[O], ca_solver.model()[U], ca_solver.model()[R]))