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
# a)
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

# plt.figure(figsize=(8, 6))
# plt.streamplot(X, Y, U, V, density=2)
# # plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=10)
# plt.plot(1, 0, 'ro', label='Kilde')
# plt.plot(-1, 0, 'bo', label='Sluk')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# # plt.axis('equal')
# plt.show()


# b)
# from scipy import integrate

h = 0.01
# t = np.arange(-2, 2, h)
# x = np.zeros(len(t))
# y = np.zeros(len(t))

# # Startverdi for (x, y) i (1, 0). y[0] er allerede 0
# x[0] = 1

def vx(x, y):
    r1_sq_s = (x - 1)**2 + y**2
    r2_sq_s = (x + 1)**2 + y**2
    return L*(x - 1)/r1_sq_s - M*(x + 1)/r2_sq_s

def vy(x, y):
    r1_sq_s = (x - 1)**2 + y**2
    r2_sq_s = (x + 1)**2 + y**2
    return L*y/r1_sq_s - M*y/r2_sq_s

# print(type(vx(x[0], y[0])))
# print(type(vy(x[0], y[0])))

# for i in range(len(t) - 1):
#     x[i+1] = x[i] + h * vx(x[i], y[i])
#     y[i+1] = y[i] + h * vy(x[i], y[i])

# plt.plot(x, y)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()


# AI
# start_x = [0.9, 0.9, 0.9, 0.9, 0.9]
# start_y = [-0.2, -0.1, 0, 0.1, 0.2]


# for j in range(len(start_x)):

#     x = start_x[j]
#     y = start_y[j]

#     x_bane = [x]
#     y_bane = [y]

#     for i in range(100000):

#         x_ny = x + h*vx(x, y)
#         y_ny = y + h*vy(x, y)

#         x = x_ny
#         y = y_ny

#         x_bane.append(x)
#         y_bane.append(y)

#         if np.sqrt((x+1)**2 + y**2) < 0.05:
#             break

#     plt.plot(x_bane, y_bane)

# plt.plot(1, 0, 'ro', label='Kilde')
# plt.plot(-1, 0, 'bo', label='Sluk')

# plt.xlabel('x')
# plt.ylabel('y')
# plt.axis('equal')
# plt.legend()
# plt.grid()
# plt.show()

# d)
# import sympy as sp
# from sympy import plot_implicit

# # Definer variablene
# x, y = sp.symbols('x y')

# # Definer potensialfunksjonen
# phi = (sp.log(sp.sqrt((x-1)**2 + y**2))
#        - sp.log(sp.sqrt((x+1)**2 + y**2)))

# # Velg verdier for nivåkurvene
# nivaaer = np.linspace(-1, 1, 20)

# # Tegn nivåkurvene
# tegn = None

# for c in nivaaer:
#     new_plot = plot_implicit(
#         sp.Eq(phi, c),
#         (x, -4, 4),
#         (y, -4, 4),
#         show=False
#     )

#     if tegn is None:
#         tegn = new_plot
#     else:
#         tegn.extend(new_plot)

# tegn.show()



# =============================================
#                   Oppgave 6
# =============================================
import sympy as sp

# Lager en symbolsk variabel t
t = sp.symbols('t')

# Definerer x(t) og y(t)
x = 4 * sp.cos(t)**3
y = 12 * sp.sin(t)**3

# Deriverer x med hensyn på t
dx = sp.diff(x, t)

# Setter opp integranden
integrand = -y * dx

# Integrerer fra 0 til 2*pi
areal = sp.integrate(integrand, (t, 0, 2*sp.pi))

# Skriver ut eksakt og numerisk svar
print("Eksakt areal:", areal)
print("Desimaltall:", float(areal))