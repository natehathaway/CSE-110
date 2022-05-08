



import math
from turtle import circle, width

#Square Area
square = float(input("What is the length of a side of the square? "))
area = square **2
print(f"The area of the square is: {area}")


#Rectangle Area
length = float(input("What is the length of the rectangle? "))
width = float(input("What is the width of the rectangle? "))
rectangle = length * width
print(f"The area of the rectangle is: {rectangle}" )

#Circle Area
radius = float(input("What is the radius of the circle? "))
circle = radius * math.pi
print(f"The area of the circle is: {circle}")


#Stretch goal 2
length = float(input("Please input a length value: "))
square1 = length **2
circle1 = length * math.pi 
cube = length ** 3
sphere = (4/3) * math.pi * length **3

print(f"The area of the square is: {square1}")
print(f"The area of the circle is : {circle1}")
print(f"The volume of the cube is : {cube}")
print(f"The volume of the sphere is : {sphere}")


##Stretch goal 3
#Square Area
square2 = float(input("What is the length of a side of the square in centimeters? "))
area2 = square2 **2
area2_meters = area2 / 10000
print(f"The area of the square is: {area2} cm^2, or {area2_meters} m^2")


#Rectangle Area
length2 = float(input("What is the length of the rectangle in centimeters? "))
width2 = float(input("What is the width of the rectangle in centimeters? "))
rectangle2 = length2 * width2
rectangle2_meters = rectangle2 / 10000
print(f"The area of the rectangle is: {rectangle2} cm^2, or {rectangle2_meters} m^2" )

#Circle Area
radius2 = float(input("What is the radius of the circle in centimeters? "))
circle2 = radius2 * math.pi
circle_meters = circle2 / 10000
print(f"The area of the circle is: {circle2} cm^2, or {circle_meters} m^2")

