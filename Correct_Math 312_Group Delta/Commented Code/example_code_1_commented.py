import numpy as np #importing packages needed for problem
import matplotlib.pyplot as plt #importing packages needed to graph problem

def f(x, y): #define a function f
    return x + y #returns the output when the function is run

x0 = 0.0 #set initial value
y0 = 1.0 #set initial value


h = 0.1 #set step size to .1
n = 100 #set n to 100


x_values = np.zeros(n+1) #use the numpy package to return an array of x values
y_values = np.zeros(n+1) #use the numpy package to return an array of y values

x_values[0] = x0 #sets initial condition of x(0)=0
y_values[0] = y0 #sets initial condition of x(0)=0

for i in range(n): #for each number in the range 0-100, complete the following calculations
    x = x_values[i] #x is equal to x sub i
    y = y_values[i] #y is equal to y sub i
    y_prime = f(x, y) #plug x and y values into derivative
    x_values[i+1] = x + h #x sub i+1 is equal to x plus the step size
    y_values[i+1] = y + h * y_prime #y sub i+1 is equal to y plus y' times the step size

#use matplotlib to set the specifics of the figure
plt.figure(figsize=(8, 6))#set the size of the figure
plt.plot(x_values, y_values, label='Euler\'s Method') #plot the x and y values
plt.xlabel('x') #label x axis
plt.ylabel('y') #label y axis
plt.legend() #create a legend in the plot
plt.title('Euler\'s Method for dy/dx = x + y') #set title
plt.grid(True) #sets grid behind figure
plt.show() #show plot in output

