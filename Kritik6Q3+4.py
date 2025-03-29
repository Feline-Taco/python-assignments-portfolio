import numpy as np
import matplotlib.pyplot as plt

# Q3:
def normal_density(mean, var, x): #AKA fX
    Lowerpart = 1/(var*np.sqrt(2*np.pi))
    Upperpart = np.exp(-0.5*(((x-mean)/var)**2))
    return Lowerpart * Upperpart

def plotter(mean, var, fX):
    x = np.linspace(0,100,200)
    y = fX(mean, var, x)
    plt.plot(x, y)
    plt.grid()
    plt.show()

def quadrature_int(mean, var, a, b, fX): #IGNORE THIS
    return (b-a)*(fX(mean,var,a)+fX(mean,var,b))/2

def composite_int(mean, var, a, b, fX): #Uses composite numerical integration technique
    n = 10*round(b-a) #Number of total steps
    Val = 0 #Initial value of sum
    for i in range(1, n-1):
        Val+=fX(mean, var, (a+i*((b-a)/n)))
    return  (((b-a)/n)*((fX(mean,var,a)/2)+ Val + (fX(mean,var,b)/2))) #adds all together

#print (quadrature_int(171, 7.1, 162, 190,normal_density))

print (composite_int(171, 7.1, 162, 190,normal_density))
plotter(50, 7.5, normal_density)

# Q4a is attached as a png

# Q4b is attached as a png

# Q4c:
def normal_distribution_expected_value(mean, var, f):
    n = 100000
    a = mean - 4 * np.sqrt(var)
    b = mean + 4 * np.sqrt(var)
    x = np.linspace(a, b, n + 1)
    delta_x = (b - a) / n
    integral = 0
    for i in range(n):
        integral +=  2.38*(x[i]**2)*f(mean, var, x[i])*delta_x
    return integral

avg_dose = normal_distribution_expected_value(171,7.1,normal_density)

print(avg_dose)

print(2.38*(171**2))