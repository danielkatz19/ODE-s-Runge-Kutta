import numpy as np
import matplotlib.pyplot as plt

#@Creator Daniel Katz

def euler_method_system(f, g, R0, F0, h, num_steps, a, b, y, d, K):
    t_values = [0]
    R_values = [R0]
    F_values = [F0]
    
    for _ in range(num_steps):
        R_next = R_values[-1] + (h * f(R_values[-1], F_values[-1], a, b, K))

        F_next = F_values[-1] + (h * g(R_values[-1], F_values[-1], y, d))
        t_next = t_values[-1] + h

        t_values.append(t_next)
        R_values.append(R_next)
        F_values.append(F_next)
    
    return t_values, R_values, F_values


def f(R, F, a, b, K):
    return (a*R*(1 - (R/K))) - (b*R*F)


def g(R, F, y, d):
    return -d*F + y*R*F

R0 = 10
F0 = 1

a = 2
b = 1
y = 1
d = 5
K = 10
num_steps = 100

t_end = 10

h = (t_end) / num_steps

t_values, R_values, F_values = euler_method_system(f, g, R0, F0, h, num_steps, a, b, y, d, K)

plt.figure(figsize=(10, 10))
plt.plot(t_values[:-1], R_values[:-1], label="Rabbits")
plt.plot(t_values[:-1], F_values[:-1], label="Foxes")
plt.xlabel('Time')
plt.ylabel('Population')
plt.title("Euler's Method for System of ODEs")
plt.legend()
plt.grid(True)
plt.show()
