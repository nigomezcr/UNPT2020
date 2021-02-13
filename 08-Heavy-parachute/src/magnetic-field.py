import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad, dblquad

R = 1
M = 1
L = 1
MU0 = 1#4 * np.pi * 1e-5  # in T cm / A units

#Integrand
def f(r_prim, z_prim, r, z):

    norm = np.sqrt((r - r_prim)**2 + (z - z_prim)**2)
 #   return norm
    a = 3 * (z - z_prim)**2
    a = a / (norm**5)

    b = 1 / (norm**3)

    return (0.5 * M * MU0 * r_prim ) * (a - b)

#Magnetic field
def B(r,z):
    
    return dblquad(lambda t, x: f(t,x,r,z), 0, L, lambda x: 0, lambda x: R)[0]

#Analytical solution
def Banal(z):
    return 0.5*M*MU0*(z/np.sqrt(z**2 + R**2) - (z-L)/np.sqrt((z-L)**2 + R**2))


def Axischeck():

    z_array = np.arange(L,4*L,0.1)
    r_array = np.arange(L,4*L,0.1)
    Baz = np.zeros(30)
    Bz = np.zeros(30)
    
    for i in range(30):
        z = z_array[i]
        Bz[i] = B(0,z)
        Baz[i]= Banal(z)
        #print(z, B(0,z))
    
    
    plt.plot(z_array, Bz, 'b')
    plt.plot(z_array, Baz, 'gray', linestyle='dashed')
    
    
def Table1():        
    z_values = np.linspace(L+.1, 10*L, 51)
    r_values = np.array([R+0.1] + [0.5 * (1.2**i) for i in range(18)])
    
    table = []
    
    for z in z_values:
        row = []
        for r in r_values:
            row.append(B(r,z))
    
        table.append(row)
    
    table = np.array(table)
    
    
    np.savetxt("magnetic-data.txt", table)

    
def Flux(a,h):
    integral = quad(lambda x: B(x,h)*x, 0, a)[0]
    return 2*np.pi*integral

   
def Table2():        
    h_values = np.linspace(L+.1, 10*L, 51)
    a_values = np.linspace(1,10,5)
    
    table = []
    
    for h in h_values:
        row = []
        for a in a_values:
            row.append(Flux(a,h))
    
        table.append(row)
    
    table = np.array(table)
    
    
    np.savetxt("flux-data.txt", table)

Table2()


"""
def int2d(func, x_min, x_max, h, y_min, y_max, k, *args):
    

    def ff(x, y): return func(x, y, *args)

    x_num = int((x_max - x_min) / h)
    y_num = int((y_max - y_min) / k)

    x = np.linspace(x_min, x_max, x_num)
    y = np.linspace(y_min, y_max, y_num)

    integral = 0
    for i in x:
        for j in y:
            A = ff(i-h, j-k) + ff(i+h, j-k) + \
                ff(i-h, j+k) + ff(i+h, j+k)

            B = ff(i, j-k) + ff(i, j+k) + ff(i-h, j) + ff(i+h, j)

            C = ff(i, j)

            integral += A + 4*B + 16*C

    return k*h*integral / 9
"""



