import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

def func_1(x, y):
    return x**2+y**2

def func_2(x, y):
    return 1 - np.exp(-x**2-(y-2)**2)-2*np.exp(-x**2-(y+2)**2)

def grad_func_1(x, y):
    return 2*x, 2*y

def grad_func_2(x, y):
    grad_x = 2 * x * np.exp(-x ** 2 - (y - 2) ** 2) + 4 * x * np.exp(-x ** 2 - (y + 2) ** 2)
    grad_y = (2 * (y - 2)) * np.exp(-x ** 2 - (y - 2) ** 2) + (4 * (y + 2)) * np.exp(-x ** 2 - (y + 2) ** 2)
    return grad_x, grad_y

def grad_descent(x0, y0, grad_f, alpha, num_iterations):
    x, y = x0, y0
    grad_x, grad_y = grad_f(x, y)
    i = 0
    # while i < num_iterations and abs(grad_x) > 1e-5 and abs(grad_y) > 1e-5:
    #     x = x - alpha * grad_x
    #     y = y - alpha * grad_y
    #     grad_x, grad_y = grad_f(x, y)
    #     i += 1
    
    for i in range(num_iterations):
        x = x - alpha * grad_x
        y = y - alpha * grad_y
        grad_x, grad_y = grad_f(x, y)
    return float(x), float(y)


#4b
print(grad_descent(0.1, 0.1, grad_func_1, 0.1, 10))
print(grad_descent(-1, 1, grad_func_1, 0.01, 100))

#4c
print(grad_descent(0, 1, grad_func_2, 0.01, 10000))
print(grad_descent(0, -1, grad_func_2, 0.01, 10000))

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x,y = np.meshgrid(x,y)
z = func_2(x, y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')