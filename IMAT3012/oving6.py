# # ============================================
# #                 Oppgave 3
# # ============================================
# # a)

# # Ligningssystem med linalg.solve
# import numpy as np

# N = 6
# h = 1/N

# A = np.zeros((N-1, N-1))
# b = np.zeros(N-1)

# # Sett opp matrisen
# for i in range(N-1):
#     A[i, i] = -2

#     if i > 0:
#         A[i, i-1] = 1

#     if i < N-2:
#         A[i, i+1] = 1

# # Randbetingelser
# b[0] = -100
# b[-1] = -200

# # Løs likningssystemet
# u_interior = np.linalg.solve(A, b)

# # Legg til randverdiene
# u = np.concatenate(([100], u_interior, [200]))

# x = np.linspace(0, 1, N+1)

# print(f"linalg.solve løsning: {u}")
# print(f"u(0.33) = {u[np.argmin(abs(x - 0.33))]}\n")





# # Jacobi
# N = 6

# # Startverdier
# u = np.ones(N+1) * 100

# # Randbetingelser
# u[0] = 100
# u[N] = 200

# tol = 1e-10
# max_iter = 10000

# for k in range(max_iter):

#     u_new = u.copy()

#     for i in range(1, N):
#         u_new[i] = (u[i-1] + u[i+1]) / 2

#     # Sjekk om vi har konvergert
#     if np.max(np.abs(u_new - u)) < tol:
#         u = u_new
#         break

#     u = u_new

# print(f"Jacobi løsning: {u}")
# print("Antall iterasjoner:", k+1)
# print(f"u(0.33) = {u[np.argmin(abs(x - 0.33))]}\n")




# # Gauss-Seidel
# N = 6

# u = np.ones(N+1) * 100

# u[0] = 100
# u[N] = 200

# tol = 1e-10
# max_iter = 10000

# for k in range(max_iter):

#     u_old = u.copy()

#     for i in range(1, N):
#         u[i] = (u[i-1] + u[i+1]) / 2

#     if np.max(np.abs(u - u_old)) < tol:
#         break

# print(f"Gauss-Seidel løsning: {u}")
# print("Antall iterasjoner:", k+1)
# print(f"u(0.33) = {u[np.argmin(abs(x - 0.33))]}\n")



# # b)
# N = 100
# h = 1 / N

# x = np.linspace(0, 1, N + 1)

# A = np.zeros((N - 1, N - 1))
# b = np.zeros(N - 1)

# for i in range(N - 1):
#     A[i, i] = -2
#     if i > 0:
#         A[i, i - 1] = 1
#     if i < N - 2:
#         A[i, i + 1] = 1

# for i in range(1, N):
#     b[i - 1] = -h**2 * np.sin(x[i])

# b[0] -= 1.1
# b[-1] -= 1.2
# u_interior = np.linalg.solve(A, b)

# u = np.zeros(N + 1)
# u[0] = 1.1
# u[-1] = 1.2
# u[1:-1] = u_interior


# print(f"\nlinalg.solve for oppgave b) = {u[np.argmin(np.abs(x - 0.66))]}")



# ============================================
#                 Oppgave 4
# ============================================
# a)
import numpy as np
import matplotlib.pyplot as plt

C = 0.25
N = 100
L = 2
dx = L / (N + 1)
dt = 0.5 * (dx**2 / C**2)
r = C**2 * dt / dx**2

x = np.linspace(0, L, N + 2)

u = np.zeros(N + 2)

u[0] = 10
u[-1] = 0

t = 0
t_end = 20

sol = []
times = []

while t <= t_end:
    u_new = u.copy()
    for i in range(1, N + 1):
        u_new[i] = u[i] + r * (u[i+1] - 2 * u[i] + u[i-1])
    u = u_new
    t += dt
    sol.append(u.copy())
    times.append(t)

print(times)
for i in range(0, len(times), max(1, len(times)//10)):
    plt.plot(x, sol[i], label=f't = {times[i]:.2f}')
plt.xlabel("x")
plt.ylabel("Temperatur")
plt.legend()
plt.grid()
plt.show()
