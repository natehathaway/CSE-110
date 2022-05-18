import math
#Intro Statement

print("Welcome to the velocity calculator. Please enter the following: ")

#Equation: v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))

#Inputs

m = float(input("Mass (in kg): "))
g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
t = float(input("Time (in seconds): "))
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
A = float(input("Cross sectional area (in m^2): "))
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

#Outputs
c = 1 / 2 * p * A * C
Vt = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))
print(" ")
print(f"The inner value of c is: {c:.3f}")
print(f"The velocity after {t:.1f} seconds is: {Vt:.3f} m/s")