import numpy as np
import matplotlib.pyplot as plt

#Halfstep method for dy/dx = x - y with subinterval N = 10
#x0 = 1, y0 = 1, solves for x = 2

def f(x, y):
    return x - y

def midpoint_method(f, x0, y0, stop_x, n):
    x_values = [x0]
    y_values = [y0]

    step_size = (stop_x - x0) / n

    for _ in range(n):
        x_current = x_values[-1]
        y_current = y_values[-1]

        # Halfstep
        k1 = step_size * f(x_current, y_current)
        k2 = step_size * f(x_current + 0.5 * step_size, y_current + 0.5 * k1)

        # Update values
        x_next = x_current + step_size
        y_next = y_current + k2

        x_values.append(x_next)
        y_values.append(y_next)

    return x_values, y_values

x0 = 1
y0 = 1

stop_x = 2  # Stopping value for x
n = 10  # Number of subintervals

x_values, y_values = midpoint_method(f, x0, y0, stop_x, n)

# Print the solution
solution_vector = np.array([x_values, y_values]).T
print(f"Solution Vector for {n} subintervals:")
print(solution_vector)

#calcualtes for n = 1000, if needed, comment back in
#x_values, y_values = midpoint_method(f, x0, y0, stop_x, 1000)


# Plotting the solution
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label="Halfstep method")
plt.xlabel('x')
plt.ylabel('y')
plt.title("Halfstep Method for dy/dx = x - y")
plt.legend()
plt.grid(True)
plt.show()
