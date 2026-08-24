# import numpy as np

# def nest(c: list, x: float) -> int:
#     res = c[0]
#     for i in range(len(c)-1):
#         res = x * res + c[i+1]
#     return res


# def test_feil(funk):
#     c = np.ones(51) #sjekk ut numpy funksjonen ones :)
#     x = 1.00001
#     Px = (x**51 - 1) / (x - 1) #Ekvivalent uttrykk for polynom fra oppgavetekst, evaluert i x=1.00001
#     return(abs(Px-funk(c,x)))



# c = [int(element) for element in list("32466")]
# # c = [3, 2, 4, 6, 6]
# x = 1/3
# print(nest(c, x))
# print()
# print(test_feil(nest))


# import numpy as np

# sec = lambda x: 1.0/np.cos(x)
# f_orig = lambda x: (1-sec(x)) / (np.tan(x))**2 #<------- Utrykk fra oppgaveteksten her
# f_ny = lambda x: -np.cos(x) / (1+np.cos(x)) #<------------Omformet uttrykk her

# x = [10**(-i) for i in range(1,15)]

# print("{:<10}{:<30}{:<30}{:<20}".format("x", "Original", "Omskrevet", "Korrekte desimalplasser"))
# print("------------------------------------")
# for xi in x:
#    fx_orig = f_orig(xi)
#    fx_ny = f_ny(xi)
#    korrekte = -np.floor(np.log10(np.abs(fx_orig-fx_ny)))-1
#    print("{:<10}{:<30}{:<30}{:<20}".format(xi, fx_orig, fx_ny,korrekte))


import numpy as np


def fikspunkt_solve(f, x0, tol):
   # Dine kode her --->
   x_ny = f(x0)
   print("Starter nå while-loop")
   while abs(x0 - x_ny) > tol:
      x0 = x_ny
      x_ny = f(x_ny)
   return x_ny

f1 = lambda x: (2*x + 2)**(1 / 3) #Hvilken funksjon skal inn i fikspunkt_solve? (lign. 1)
f2 = lambda x: np.log(7 - x) #Hvilken funksjon skal inn i fikspunkt_solve? (lign. 2)
f3 = lambda x: np.log(4 - np.sin(x)) #Hvilken funksjon skal inn i fikspunkt_solve? (lign. 3)
funcs = [f1,f2,f3]
maks_feil = 10**(-8) #????
sols = []
for f in funcs:
   x_sol = fikspunkt_solve(f, 2.0, maks_feil)
   sols.append(x_sol)

print(f"Løsning til første ligning x = {sols[0]}")
print(f"Løsning til andre ligning x = {sols[1]}")
print(f"Løsning til tredje ligning x = {sols[2]}")