import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return x ** 2
def f2(x):
    return x ** 4 - 2 * x ** 2
def f3(x):
    if x > 0:
        return x ** x
    elif x == 0:
        return 1
    else:
        return abs(x) ** abs(x)
def f4(x):
    return abs(x)

def fprime(f, x): #Estimate of derivative
    return (f(x + 10 ** -10) - f(x - 10 ** -10)) / (2 * 10 ** -10)

def Minfinder(f, x0, learning_rate):
    x_coords = [x0]
    y_coords = [f(x0)]
    
    i = 1 #counter

    # Gets x and y close to min till derivative almost 0
    #stop looking after too many iterations (in case of overshoot)
    while i < 10 ** 3 and abs(fprime(f, x_coords[i - 1])) > 10 ** -10:
        # Moves x coord closer to min point
        x_coords.append(x_coords[i - 1] - learning_rate * fprime(f, x_coords[i - 1]))
        y_coords.append(f(x_coords[i]))  # Moves y coord closer to min point
        i += 1  #Add more to count

    #plotting
    plot_range = np.linspace(min(x_coords) - 0.5, max(x_coords) + 0.5, 10000)  #For nice plot
    Funcrange = [f(i) for i in plot_range]
    plt.plot(plot_range, Funcrange)  # this plots the function f(x)
    plt.plot(x_coords, y_coords)  # this will plot the sequence of points x_n, f(x_n)

    print(i)
    if i == 10 ** 3:
        return "Error! No minimum found. Try a different learning rate and/or starting x-value."
    else:
        return "Minimum of this function is at (" + str(round(x_coords[i - 1], 3)) + ", " + str(
            round(y_coords[i - 1], 3)) + ")."
    # last x_n and y_n, #rounded to three decimal places.


# controls user input, allows user to find different roots by trying different x0's and learning rates
def main():
    done = False

    while not done:
        function_name = (input("Enter a which function you want to minimize (1, 2, 3, 4): "))

        function = None

        if function_name == "1":
            function = f1
        elif function_name == "2":
            function = f2
        elif function_name == "3":
            function = f3
        elif function_name == "4":
            function = f4
        x0 = float(input("Enter a starting x-value for the optimization: "))
        learning_rate = float(input("Enter a learning rate for the optimization: "))

        print(Minfinder(function, x0, learning_rate))
        continue_or_not = input("Would you like to continue (yes or no): ")

        if continue_or_not.lower() == "no":
            done = True


main()