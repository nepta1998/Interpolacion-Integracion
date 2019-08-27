import numpy as np
from sympy import *

x = Symbol('x')
#calculamos el metodo de simpson
def simpson(rango1,rango2,n,y):
    dx=(rango2-rango1)/n
    x = Symbol('x')
    fx = lambdify(x, y, 'numpy')
    suma=0
    for i in range(0,n+1):
        if(i==0):
            suma=suma+fx(rango1)
        else:
            if(i==n):
                suma = suma+fx(rango2)
            else:
                if(i%2==0):
                    suma=suma+2*fx(rango1+i*dx)
                else:
                    suma = suma+4*fx(rango1+i*dx)
    return dx/3*suma


#calculamos el metodo del trapecio
def trapecio(rango1, rango2, n, y):
    dx = (rango2-rango1)/(2*n)
    print(dx)
    w = np.linspace(rango1, rango2, num=n+1)
    x = Symbol('x')
    fx = lambdify(x, y, 'numpy')
    suma = 0
    for i in range(0,n+1):
        if(i!=0 and i!=n):
            suma=suma+2*fx(w[i])
        else:
           suma = suma+fx(w[i])
    print(suma)
    return dx*suma


