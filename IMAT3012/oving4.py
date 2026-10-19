# =============================================
#                   Oppgave 1
# =============================================
# import numpy as np
# from scipy.spatial import Delaunay

# # Antall punkter
# N = 100000

# # Definerer de ulike punktene for hver dimensjon
# theta = 2 * np.pi * np.random.rand(N)
# radius = 2 * np.random.rand(N)
# z = 4 * np.random.rand(N)

# # Lage koordinatmatrise med punktene, hhv. [x, y, z]-koordinater
# pts = np.column_stack((radius * np.cos(theta), radius * np.sin(theta), z))

# # Triangulering av punktene; gir tetraedere
# tri = Delaunay(pts)

# # Definereing av hvert hjørne i tetraedrene
# p = pts[tri.simplices[:, 0]]
# q = pts[tri.simplices[:, 1]]
# r = pts[tri.simplices[:, 2]]
# s = pts[tri.simplices[:, 3]]
# n = len(p)
# # Vi lager tre vektorer fra p-hjørnet i hvert tetraeder til hver av de andre punktene i hver tetraeder
# u = q - p
# v = r - p
# w = s - p

# # Legger vektorene i en 3x3-matrise
# M = np.column_stack((u, v, w)).reshape(n, 3, 3)

# # Beregner volumet til hver tetraeder
# dV = np.abs(np.linalg.det(M)) / 6

# # Summerer opp alle volumene
# res = np.sum(dV)
# print(f"Resultat er : \n {res}")

# =============================================
#                   Oppgave 2
# =============================================
# from sympy import symbols, cos, sin
# from sympy.plotting import plot3d_parametric_line
# import matplotlib.pyplot as plt
# import numpy as np

# t = symbols("t")
# # p = plot3d_parametric_line(6 * sin(t), 6 * cos(t), 4 * t, (t, 0, 4))

# from scipy.integrate import quad
# r = lambda r: 2*np.sqrt(13)

# res = quad(r, 0, 4)
# print(res)

# =============================================
#                   Oppgave 3
# =============================================
import sympy as sp
from scipy.integrate import quad

t = sp.symbols("t")

a = 1.00005507808
b = 0.55342925736
c = 0.99873327689

x = 1-(c*(1-t)**3 + 3*b*t*(1-t)**2)
y = 1-(a*t**3 + 3*b*t**2*(1-t))

# sp.plot_parametric((x,y), (t,0,1))

dx = sp.diff(x, t)
dy = sp.diff(y, t)

speed = sp.sqrt(dx**2 + dy**2)
f = sp.lambdify(t, speed, "numpy")

L, error = quad(f, 0, 1)
print(L)
print(error)