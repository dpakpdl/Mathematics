import numpy as np
from scipy.optimize import linprog

A = np.array([[-1, -1, -1], [-1,2, 0], [0, 0, -1], [-1, 0, 0], [0, -1, 0]])
b = np.array([-1000, 0, -340, 0, 0])
c = np.array([10,15,25])

res = linprog(c, A_ub=A, b_ub=b,bounds=(0, None))

print('Optimal value:', res.fun, '\nX:', res.x)
# ('Optimal value:', 15100.0, '\nX:', array([ 660.,    0.,  340.]))
