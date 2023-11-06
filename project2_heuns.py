import numpy as np
import matplotlib.pyplot as plt

#heuns method with the variables a,b,y,d,K

#@Creator Daniel Katz

def heun_method_system(dR, dF, R0, F0, h, num_steps, a, b, y, d, K):
    #np.arange in order, (start, stop, steps)
    t_values = [0]
    R_values = [R0]
    F_values = [F0]
    
    for _ in range(num_steps):
        #predictor
        R_next_euler = R_values[-1] + (h * dR(R_values[-1], F_values[-1], a, b, K))
        F_next_euler = F_values[-1] + (h * dF(R_values[-1], F_values[-1], y, d))
        

        #corrector
        R_next = R_values[-1] + (h/2) * (dR(R_values[-1], F_values[-1], a, b, K) + dR(R_next_euler, F_next_euler, a, b, K))
        F_next = F_values[-1] + (h/2) * (dF(R_values[-1], F_values[-1], y, d) + dF(R_next_euler, F_next_euler, y, d))
        t_next = t_values[-1] + h
        
        t_values.append(t_next)
        R_values.append(R_next)
        F_values.append(F_next)
    
    return t_values, R_values, F_values

def dR(R, F, a, b, K):
    return a*R*(1 - (R/K)) - (b*R*F)

def dF(R, F, y, d):
    return ((-d)*F) + (y*R*F)

R0 = 10
F0 = 1

#alpha
a = 2

#beta
b = 1

#gamma
y = 1

#delta
d = 5

K = 10


num_steps = 100
t_end = 10

h = (t_end) / num_steps

t_values, R_values, F_values = heun_method_system(dR, dF, R0, F0, h, num_steps, a, b, y, d, K)

plt.figure(figsize=(10, 10))
plt.plot(t_values[:-1], R_values[:-1], label="Rabbits")
plt.plot(t_values[:-1], F_values[:-1], label="Foxes")
plt.xlabel('Time')
plt.ylabel('Population')
plt.title("Heun's Method for System of ODEs")
plt.legend()
plt.grid(True)
plt.show()