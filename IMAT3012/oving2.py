# from scipy.integrate import dblquad

# def f(x, y):
#     return x**2 + y**2

# res, err = dblquad(f, -3, 3, -4, 4)

# print(res)
# print(err)



# ==================================================
#                   Oppgave 7
# ==================================================

# Beregning av arealet av en disk med radius 1.0
# import random as rnd
# numSim = 10**6
# numHit = 0
# xmin = 0
# xmax = 2.0
# ymin = 2.0
# ymax = 4.0

# for i in range(numSim):
#     x = rnd.random() * (xmax - xmin) + xmin # -1.0..1.0
#     y = rnd.random() * (ymax - ymin) + ymin # -1.0..1.0
#     d = x*x + y*y
#     if(d < 1.0):
#         numHit += 1

# area = (xmax - xmin) * (ymax - ymin)
# print("Svar:", area * numHit / numSim)


# ==================================================
#                   Oppgave 8
# ==================================================
# a)

# import numpy as np

# xmin = -1
# xmax = 1
# ymin = -2
# ymax = 2

# numx = numy = 1000
# dx = (xmax - xmin) / numx
# dy = (ymax - ymin) / numy
# dA = dx*dy

# xv = np.linspace(xmin, xmax, numx, endpoint=False)
# yv = np.linspace(ymin, ymax, numy, endpoint=False)
# x, y = np.meshgrid(xv, yv)

# np.sum(np.exp(x**2 + y**2) * dA)

# # b)
# xminB = -1
# xmaxB = 1
# yminB = -1
# ymaxB = 1

# numxB = numyB = 1000
# dxB = (xmaxB - xminB) / numxB
# dyB = (ymaxB - yminB) / numyB
# dAB = dxB*dyB

# xvB = np.linspace(xminB, xmaxB, numxB, endpoint=False)
# yvB = np.linspace(yminB, ymaxB, numyB, endpoint=False)
# xB, yB = np.meshgrid(xvB, yvB)

# px = x[x*x + y*y < 1]
# py = y[x*x + y*y < 1]

# print(np.sum(np.sin(px**2 + py)*dAB))


# ==================================================
#                   Oppgave 9
# ==================================================
# from scipy.integrate import dblquad
# from math import sin

# Ia = dblquad(lambda x, y: x * y**2, 0, 1, 2, 3)
# Ib = dblquad(lambda y, x: sin(x**4 + 2 * y**2), 0, 1, -1, 1)
# Ic = dblquad(lambda x, y: x * y**2, 0, 1, 0, lambda x: x)
# Id = dblquad(lambda y, x: sin(x**4 + 2 * y**2), 0, 1, 0, lambda x: 1-x)


# ==================================================
#                   Oppgave 10
# ==================================================
# a)

import sympy as sp

x, y = sp.symbols("x, y")
a = sp.symbols("a", positive=True)

# f = x**2 * y

# print(sp.integrate(f, (y, -sp.sqrt(a**2 - x**2), 0), (x, -a, a)))


# b )
f = x + a   # Delta z: (x + a) - 0

V = sp.integrate(f,
                 (x, -sp.sqrt(a**2 - y**2), sp.sqrt(a**2 - y**2)),
                 (y, -a, a))

print(V)