import numpy as np
from scipy import linalg
c = np.array([[0,0,1],[256,16,1],[64,8,1]])
d = np.array([0,0,8])
x = linalg.solve(c,d)
#[-.125,2,0]
print(x)
