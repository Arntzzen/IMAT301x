# =============================================
#                 Oppgave 1
# =============================================
# import sympy as sp

# r, theta = sp.symbols("r, theta")
# integrand = sp.sqrt(1 + 4 * r**2) * r
# I = sp.integrate(integrand,
#                  (r, 0, 2),
#                  (theta, 0, 2 * sp.pi))
# print(I.evalf())

# import numpy as np
# from scipy.spatial import Delaunay
# import matplotlib.pyplot as plt

# numpts = 1000
# pts = np.zeros((numpts,3))
# pts[:,:2] = np.random.uniform(-1,1,(numpts,2))
# pts[0:4, :2] = [[-1.0, -1.0],[-1.0, 1.0],[1.0, -1.0],[1.0, 1.0]]
# pts[50:100, 0] = -1.0
# pts[100:150, 0] = 1.0
# pts[150:200, 1] = -1.0
# pts[200:250, 1] = 1.0

# pts[:,2] = 4.0 - pts[:,0]**2 - pts[:,1]**2

# tri = Delaunay(pts[:,:2])
# plt.triplot(pts[:,0], pts[:,1], tri.simplices)
# plt.show()

# p = pts[tri.simplices[:,0]]
# q = pts[tri.simplices[:,1]]
# r = pts[tri.simplices[:,2]]

# u = q - p
# v = r - p

# a = np.cross(u, v)
# area = np.sum(np.linalg.norm(a, axis=1))/2

# print(area)

# =============================================
#                   Oppgave 2
# =============================================
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

L = 1
M = 3

r1_sq = (X - 1)**2 + Y**2
r2_sq = (X + 1)**2 + Y**2

U = L*(X - 1)/r1_sq - M*(X + 1)/r2_sq
V = L*Y/r1_sq - M*Y/r2_sq

plt.figure(figsize=(8, 6))
plt.streamplot(X, Y, U, V, density=2)
# plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=10)
plt.plot(1, 0, 'ro', label='Kilde')
plt.plot(-1, 0, 'bo', label='Sluk')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
# plt.axis('equal')
plt.show()