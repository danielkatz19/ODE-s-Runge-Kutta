import numpy as np   
import matplotlib.pyplot as plt

def f(x, y):
    return x - y

def euler_method(f, x0, y0, h, num_steps):
    x_values = [x0]
    y_values = [y0]
    
    for _ in range(num_steps):
        x_next = x_values[-1] + h
        y_next = y_values[-1] + h * f(x_values[-1], y_values[-1])
        
        x_values.append(x_next)
        y_values.append(y_next)
    
    return x_values, y_values

x0 = 1
y0 = 1

h = 0.1
num_steps = 100

x_values, y_values = euler_method(f, x0, y0, h, num_steps)

plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label="Euler's Method")
plt.xlabel('x')
plt.ylabel('y')
plt.title("Euler's Method for dy/dx = x - y")
plt.legend()
plt.grid(True)
plt.show()
