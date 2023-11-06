import numpy as np
import matplotlib.pyplot as plt

#Heun's method for original dy/dx = x - y with subinterval N = 10, N can be changed
#x0 = 1, y0 = 1, solves for x = 2

def f(x, y):
    return x - y

def heuns_method(f, x0, y0, stop_x, n):
    x_values = [x0]
    y_values = [y0]

    step_size = (stop_x - x0) / n

    for _ in range(n):
        x_current = x_values[-1]
        y_current = y_values[-1]

        # Predictor step
        y_predictor = y_current + step_size * f(x_current, y_current)

        # Corrector step
        x_next = x_current + step_size
        y_corrector = y_current + step_size * 0.5 * (f(x_current, y_current) + f(x_next, y_predictor))
        x_values.append(x_next)
        y_values.append(y_corrector)

    return x_values, y_values

x0 = 1  # Initial value for x
y0 = 1  # Initial value for y, which is e

stop_x = 2  # Stopping value for x
n = 10  # Number of subintervals

x_values, y_values = heuns_method(f, x0, y0, stop_x, n)
# Print the solution
solution_vector = np.array([x_values, y_values]).T
print(f"Solution Vector for {n} subintervals:")
print(solution_vector)

#calculates for n = 1000, if needed, comment back in
#x_values, y_values = heuns_method(f, x0, y0, stop_x, 1000) 

# Plotting the solution
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label="Heun's Method")
plt.xlabel('x')
plt.ylabel('y')
plt.title("Heun's Method for dy/dx = x - y")
plt.legend()
plt.grid(True)
plt.show()
