# # Oppgave 9
# # a)
# import sympy as sp

# t = sp.symbols("t")

# x = sp.cos(t) * 3
# y = sp.sin(t) * 2

# velx = sp.diff(x, t)
# vely = sp.diff(y, t)

# print(velx, vely)

# # b)
# x = sp.symbols("x")

# y = sp.sin(x)

# area = sp.integrate(y, (x,0,sp.pi))

# print(area)

# # Oppgave 10
# import numpy as np
# a = 10
# b = -10
# numval = 1000
# dx = (a - b) / numval
# x = np.arange(b, a, dx)
# y = np.exp(1-x**2)
# res = np.sum(y) * dx
# # print(res)

# # Oppgave 11
# from scipy import integrate

# f = lambda x: np.exp(1-x*x)
# svar, feil = integrate.quad(f, -10, 10)
# # print(f"{svar}\n{feil}")
# print(round(svar,3))

# # Oppgave 12
# import numpy as np
# import numpy.linalg as linalg

# # x og y verdier
# x_vec = np.linspace(0, 1, 100)
# y_vec = np.linspace(0, 1, 100)

# # Matrix A
# A = np.array([[1, 2], [-4, 10]])

# # a) Lag funksjonsverdiene til funksjonen 
# f = A @ [x_vec, y_vec]

# # b) Finn inversmatrisen til A.
# A_inverse = linalg.inv(A)

# # c) Finn vektoren (x,y) slik at (1,2).
# vector = np.array([1, 2])
# solution = A_inverse @ vector

# # d) Finn determinanten og den transponerte av A.
# determinant_A = linalg.det(A)
# transpose_A = np.transpose(A)


# # Oppgave 13
# import matplotlib.pyplot as plt
# import numpy as np

# # a) Lag 100 x-verdier fra 0 til 2 (Hint: Bruk np.linspace())
# xv = np.linspace(0, 2, 100)

# # b) Lag 200 y-verdier fra 0 til 4.
# yv = np.linspace(0, 4, 200)

# # c) Lag et rutenett for x og y
# x, y = np.meshgrid(xv, yv)

# # d) Lag funksjonen f
# f = np.exp(-x) * np.sin(y)

# fig = plt.figure(figsize=(15, 15))
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(x,y,f)
# plt.show()


# # Oppgave 14
# import numpy as np
# import sympy as sy

# #a)
# xv = np.linspace(1, 2, 50)
# yv = np.linspace(2, 3, 100)
# print(xv, yv)
# x, y = np.meshgrid(xv, yv)
# f = np.exp(-2 * x) * np.cos(y)

# #b)
# dx = xv[1] - xv[0]
# # fx = (np.exp(-2 * (x + dx)) * np.cos(y) - np.exp(-2 * (x-dx)) * np.cos(y)) / (2 * dx)
# fx = (f[:, 2:] - f[:, :-2]) / (2 * dx)

# #c)
# dy = yv[1] - yv[0]
# fy = (np.exp(-2 * (x)) * np.cos(y + dy) - np.exp(-2 * (x)) * np.cos(y)) / (dy)

# print(fx[10:20, 10:20])
# # print(f"\n{fy[15:25, 15:25]}")


# Oppgave 15
import matplotlib.pyplot as plt # Pakke brukt til plotting
import numpy as np # Pakke brukt til numeriske beregninger

# a) Lag 102 punkter i intervallet som starter 0 og 2pi.
t = np.linspace(0, 2*np.pi, 102)

# b) Lag x- og y-koordinaten til kurven gamma.
gamma_1 = np.exp(t)
gamma_2 = np.cos(2 * t)

plt.plot(gamma_1, gamma_2)
plt.show()