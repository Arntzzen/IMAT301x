# Ligningssystem med linalg.solve
import numpy as np

N = 6
h = 1/N

A = np.zeros((N-1, N-1))
b = np.zeros(N-1)

# Sett opp matrisen
for i in range(N-1):
    A[i, i] = -2

    if i > 0:
        A[i, i-1] = 1

    if i < N-2:
        A[i, i+1] = 1

# Randbetingelser
b[0] = -100
b[-1] = -200

# Løs likningssystemet
u_interior = np.linalg.solve(A, b)

# Legg til randverdiene
u = np.concatenate(([100], u_interior, [200]))

x = np.linspace(0, 1, N+1)

print(u)





# Jacobi
import numpy as np

N = 6

# Startverdier
u = np.ones(N+1) * 100

# Randbetingelser
u[0] = 100
u[N] = 200

tol = 1e-10
max_iter = 10000

for k in range(max_iter):

    u_new = u.copy()

    for i in range(1, N):
        u_new[i] = (u[i-1] + u[i+1]) / 2

    # Sjekk om vi har konvergert
    if np.max(np.abs(u_new - u)) < tol:
        u = u_new
        break

    u = u_new

print(u)
print("Antall iterasjoner:", k+1)




# Guass-Seidel
import numpy as np

N = 6

u = np.ones(N+1) * 100

u[0] = 100
u[N] = 200

tol = 1e-10
max_iter = 10000

for k in range(max_iter):

    u_old = u.copy()

    for i in range(1, N):
        u[i] = (u[i-1] + u[i+1]) / 2

    if np.max(np.abs(u - u_old)) < tol:
        break

print(u)
print("Antall iterasjoner:", k+1)