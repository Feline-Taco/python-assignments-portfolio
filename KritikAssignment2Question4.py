from decimal import DivisionUndefined
from re import X
import numpy as np
np.seterr(divide="ignore")

#Question 4:
def rootFinder(f,x1,x2):
    if (f(x1)*f(x2))>0: # <-- We check for roots by seeing if f(x1) and f(x2) are the same sign - If so then we assume there are no roots in the interval
            return "No roots found"

    else:
        while abs(x2-x1)>2*10**-10: # <-- This stops our function once we reach within 10^-10 of the actual root
            
            if abs(((x1+x2)/2)-x1)<2*10**-10 or abs(x2-((x1+x2)/2))<2*10**-10:
                return ((x1+x2)/2) # <-- This if statement ensures that the loop stops before the range goes less than 10^-10

            if f(x1)*f((x1+x2)/2)<0: # <-- Here we apply the bisection method and adjust our x1 or x2 values accorrdingly
                x2=((x1+x2)/2)
            elif f((x1+x2)/2)*f(x2)<0:
                x1=((x1+x2)/2)

            elif f(x1)==0: # <-- This checks if f(x1) or f(x2) are roots, and if so returns them
                return x1
            elif f(x2)==0:
                return x2
            
def func1(x):
    return (np.exp(x))+np.log(x)
def func2(x):
    return (np.arctan(x))-x**2
def func3(x):
    return (np.sin(x))/(np.log(x))
def func4(x):
    return np.log(np.cos(x))
print(rootFinder(func1,0,1))
print(rootFinder(func2,0,2))
print(rootFinder(func3,3,4))
print(rootFinder(func4,5,7))