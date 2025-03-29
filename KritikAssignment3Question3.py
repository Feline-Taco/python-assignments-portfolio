import numpy as np

def linapprox(f, c, E):
    deltaX = 10**-8
    fprime = (f(c+deltaX)-f(c-deltaX))/(2*deltaX)

    x1 = c
    Error1 = 0
    count1 = 0
    while Error1<E:
        x1 -= 0.000001
        Error1 += abs(f(x1)-f(c)-(x1-c)*fprime)
        count1 += 1
        if count1 == 5000:
            print('no x1 could be found within 5000 iterations')
            break

    x2 = c
    count2 = 0
    Error2 = 0
    while Error2<E:
        x2 += 0.000001
        Error2 += abs(f(x2)-f(c)-(x2-c)*fprime)
        count2 += 1
        if count2 == 5000:
            print('no x2 could be found within 5000 iterations')
            break

    print(str(count2) + ' '+ str(count1))
    return ('x1 = ' + str(x1) + ' and x2 = ' + str(x2))

def f(x):
    return x**2
def g(x):
    return np.sin(x)
def h(x):
    return np.exp(x)

print(linapprox(f,1,0.1))
print(linapprox(g,np.pi/4,0.05))
print(linapprox(h,0,0.01))