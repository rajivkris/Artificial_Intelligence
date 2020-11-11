from z3 import *

nqueen_solver = Solver()

def nqueen(nq: Int):
    NQ = [Int(i) for i in range(nq)]
    nqueen_solver.add([And(NQ[i] >= 0, NQ[i] < nq) for i in range(nq)])
    nqueen_solver.add(Distinct(NQ))
    nqueen_solver.add([And(NQ[i] - NQ[j] != i - j, NQ[i] - NQ[j] != j - i) for j in range(nq) for i in range(nq) if i != j])
nqueen(64)
nqueen_solver.check()
nqueen_solver.model()