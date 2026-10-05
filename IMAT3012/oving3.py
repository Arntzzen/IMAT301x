# import numpy as np

# def g (x , y , z ) :
#     return x **2 + y **2 + z **2

# n = m = l = 20 # antall deler x akse
# # m = n # antall deler y akse
# # l = n # antall deler z akse
# dx , dy , dz = 2 / n , 2 / m , 2 / l
# x = np.linnpace (-1 + dx/2, 1 - dx /2, n ) # midtpunkter x
# y = np.linnpace (-1 + dy/2, 1 - dy /2, m ) # midtpunkter y
# z = np.linnpace (-1 + dz/2, 1 - dz /2, l ) # midtpunkter z
# X , Y , Z = np.meshgrid(x, y, z, indexing='ij')

# Integralverdi = np.sum(g(X ,Y ,Z)) * dx * dy * dz
# print(Integralverdi)



# ===================== Oppgave 1 =====================
# a)
# import random as rnd

# numSim = 10**6
# numHit = 0

# for i in range(numSim):
#     x = rnd.random()
#     y = rnd.random()
#     z = rnd.random()

#     if y <= x**2 and z <= y**2:
#         numHit += 1

# area = 1 * 1 * 1
# svar = area * numHit / numSim

# print("Svar:", svar)


# b)
# from scipy.integrate import tplquad
# f = lambda z, y, x: z
# res, err = tplquad(f, 0, 1, 0, lambda x: x, 0, lambda x, y: x * y)
# print(f"Result: {res:.10f}")


# ===================== Oppgave 1 =====================
# a)
# from scipy.integrate import tplquad

# f = lambda z, y, x: x**2 + y**2 + z**2
# print(tplquad(f, -2, 2, -2, 3, -2, 2))

# # b)
# f = lambda z, y, x: 1 - (x**2 + y**2 + z**2)
# print(tplquad(f, -2, 2, -2, 3, -2, 2))

# # c)
# f = lambda x, y, z: 1
# print(tplquad(f, 0, 5, 0, lambda x: x**2, 0, lambda x, y: x**2))


# ===================== Oppgave 8 =====================
# a)
from scipy.integrate import tplquad
import numpy as np

f = lambda z, r, th: r

res, err = tplquad(f, 0, 2*np.pi,
                   lambda th: 0, lambda th: 1,
                   lambda th, r: -r, lambda th, r: r)
print(res)

# b)
f = lambda rho, phi, th: rho**2 * np.sin(phi)

res, err = tplquad(f,
                   0, np.pi / 4,
                   lambda th: np.pi / 4, lambda th: 3/4 * np.pi,
                   lambda th, phi: 0, lambda th, phi: 1 / np.sin(phi))
print(res)