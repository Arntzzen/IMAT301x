# =============================================
#                   Oppgave 1
# =============================================
import numpy as np
from scipy.spatial import Delaunay

pts = np.random.rand(10,2)
pts[:,0] *= 3.0
tri = Delaunay(pts)

p = pts[tri.simplices[:,0]]
q = pts[tri.simplices[:,1]]
r = pts[tri.simplices[:,2]]
n = len(p)

avg = 1/3 * (p + q + r)
x = avg[:,0]
y = avg[:,1]
f = x*x*y

u = q - p
v = r - p

Muv = np.column_stack((u,v)).reshape(n,2,2)
dA = np.abs(1/2*np.linalg.det(Muv))

svar = np.sum(dA*f)
print(svar)