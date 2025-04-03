import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


#4a:
def func(x,y):
    x, y = sp.symbols('x y')
    f = ((sp.exp(x))*sp.sin(y))+y**3
    df_dx = sp.diff(f,x)
    df_dy = sp.diff(f,y)
    return f, df_dx, df_dy


#4b:
def gunc(x,y):
    x, y = sp.symbols('x y')
    g = (y*x**2)+(x*y**2)
    dg_dx = sp.diff(g,x)
    dg_dy = sp.diff(g,y)
    Grad_vector = (dg_dx,dg_dy)
    magnitude = ((dg_dx**2)+(dg_dy**2))**0.5
    print(Grad_vector,magnitude)
    return Grad_vector, magnitude


#4c:
def hunc(x,y):
    x, y = sp.symbols('x y')
    h = sp.ln((x**2)+(y**2))
    dh_dx = sp.diff(h,x)
    dh_dy = sp.diff(h,y)
    d2h_dx2 = sp.diff(dh_dx,x)
    d2h_dy2 = sp.diff(dh_dy,y)
    d2h_dxdy = sp.diff(dh_dy,x)
    return d2h_dx2, d2h_dxdy, d2h_dy2
    #The symmetrical properties of second order partial derivatives only apply when all first order partial derivatives are continuous and differentiable on all R


#4d:
def junc_countour():
    x, y = sp.symbols('x y')
    j = x**3 - 3*x*y + y**3

    j_func = sp.lambdify((x, y), j, 'numpy')

    x_vals = np.linspace(-3, 3, 400)
    y_vals = np.linspace(-3, 3, 400)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = j_func(X, Y)

    plt.contourf(X, Y, Z, levels=50, cmap='viridis')
    plt.colorbar()
    plt.title('Contour plot of $j(x, y) = x^3 - 3xy + y^3$')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.show()


#4e:
def kunc_countour():
    x, y = sp.symbols('x y')
    k = y*sp.cos(x)
    k_func = sp.lambdify((x, y), k, 'numpy')

    x_vals = np.linspace(-5*np.pi, 5*np.pi, 250)
    y_vals = np.linspace(-5*np.pi, 5*np.pi, 250)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = k_func(X, Y)
    
    plt.contourf(X, Y, Z, levels=50, cmap='viridis')
    plt.colorbar()
    plt.title('Contour plot of $k(x, y) = ycos(x)$')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.show()

gunc(1,-1)
kunc_countour()