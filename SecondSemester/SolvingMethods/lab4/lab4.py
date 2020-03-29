import functions as fn
import numpy as np

t = 9
k = 3 * (2 - 4) + 2

a = 0.11 * t
b = 0.02 * k
g = 0.02 * k
d = 0.015 * t


A = np.array([[6.26 + a, 1.10 - b, 0.97 + g, 1.24 - d],
     [1.10 - b, 4.16 - a, 1.30, 0.16],
     [0.97 + g, 1.30, 5.44 + a, 2.10],
     [1.24 - d, 0.16, 2.10, 6.10 - a]])


A, S = fn.frobeus_normalization(A)
