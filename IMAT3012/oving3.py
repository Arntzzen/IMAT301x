import numpy as np

def g (x , y , z ) :
    return x **2 + y **2 + z **2

n = m = l = 20 # antall deler x akse
# m = n # antall deler y akse
# l = n # antall deler z akse
dx , dy , dz = 2 / n , 2 / m , 2 / l
x = np.linspace (-1 + dx/2, 1 - dx /2, n ) # midtpunkter x
y = np.linspace (-1 + dy/2, 1 - dy /2, m ) # midtpunkter y
z = np.linspace (-1 + dz/2, 1 - dz /2, l ) # midtpunkter z
X , Y , Z = np.meshgrid(x, y, z, indexing='ij')

Integralverdi = np.sum(g(X ,Y ,Z)) * dx * dy * dz
print(Integralverdi)