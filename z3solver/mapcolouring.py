from z3 import *

map_solver = Solver()

WA, NT, SA, Q, NSW, V, T = Ints("WA NT SA Q NSW V T")

color_map = {'0' : 'Blue', '1' : 'Red', '2' : 'Green'}

map_solver.add(WA >= 0, WA <= 2)
map_solver.add(NT >= 0, NT <= 2)
map_solver.add(SA >= 0, SA <= 2)
map_solver.add(Q >= 0, Q <= 2)
map_solver.add(NSW >= 0, NSW <= 2)
map_solver.add(V >= 0, V <= 2)
map_solver.add(T >= 0, T <= 2)

#Add distinct adjacent color contraint

map_solver.add(WA != NT, WA != SA)
map_solver.add(NT != Q, NT != SA)
map_solver.add(SA != Q, SA != NSW, SA != V)
map_solver.add(Q != NSW)
map_solver.add(NSW != V)

map_solver.check()
map_solver.model()