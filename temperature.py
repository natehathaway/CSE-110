import math
#fahrenheit to celsius
fahrenheit = float(input("What is the temperature in Fahrenheit? "))

celsius = (fahrenheit - 32) * 5 / 9

print(f"The temperature in Celsius is {celsius:.1f}")

#celsius to fahrenheit

celsius_1 = float(input("What is the temperature in Celsius? "))

fahrenheit_1 = celsius_1 * 9 / 5 + 32 
print(f"The temperature in Fahrenheit is {fahrenheit_1:.1f}")



