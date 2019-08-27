from scipy.interpolate import lagrange
import numpy as np
from sympy import *
from sympy import expand
import matplotlib.pyplot as plt


#metodo de lagrange
def MetodoLagrange2(rango1, rango2, y, n):
    x = Symbol('x')
    xi = np.linspace(rango1, rango2, num=n+1)
    fx = lambdify(x, y, 'numpy')
    fi =fx(xi)
    polinomio=0
    for i in range(0, n+1, 1):
        # Termino de Lagrange
        termino = 1
        for j in range(0, n+1, 1):
            if (j != i):
                termino = termino*(x-xi[j])/(xi[i]-xi[j])
        polinomio = polinomio + termino*fi[i]
    # Expande el polinomio
    px = polinomio.expand()
    return px,xi,fx(xi)

#metodo de lagrange usando la libreria scipy
def MetodoLagrange(rango1,rango2,y,n):
    x = Symbol('x')
    w = np.linspace(rango1, rango2, num=n+1)
    print(w)
    fx = lambdify(x, y, 'numpy')
    poli=lagrange(w,fx(w))
    return poli,w,fx(w)



#calculamos la diferencias para el metodo de newton
def diferencias(rango1,rango2,y, n):
    x = Symbol('x')
    fx = lambdify(x, y, 'numpy')
    z =np.linspace(rango1, rango2, num=n+1)
    h =fx(z)
    #print(z)
    T = h
    for k in range(1, n+1 ):
        T[k: n] = (T[k: n] - T[k - 1]) / (z[k: n] - z[k - 1])
    return T,z,fx(z)

#generamos el polinomio de newton
def polnewtonsym(diff, xx):
    x = Symbol('x')
    '''
    Calcula la expresión simbólica (algebraica) del Polinomio.
    '''
    n = len(xx) - 1
    pol = diff[n]
    for k in range(1, n + 1):
        pol = diff[n - k] + (x - xx[n - k])*pol
    return pol

#graficamos la funcion y el polinomio para ver las diferencias
def graficar(z,y,f,rango1,rango2,n,f2):
    x = Symbol('x')
    fx = lambdify(x, f, 'numpy')
    fx2 = lambdify(x, f2, 'numpy')
    w = np.linspace(rango1,rango2, 100)

    plt.subplot(221)
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.plot(z,y)
    plt.plot(z, y, 'o')
    plt.legend(['interpolacion', 'puntos'])

    plt.subplot(222)
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.plot(w, fx(w))
    plt.legend(['polinomio'])

    plt.subplot(223)
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.plot(w, fx2(w))
    plt.legend(['funcion'])

    plt.show()