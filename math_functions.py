
import math

def compute_area_square(square):
    return square * square
    

def compute_area_rectangle(width, height):
    return width * height
   

def compute_area_circle(radius):
    return math.pi * radius * radius

shape = ""  


while shape.lower() != "quit":
    shape = input("Pick one: square, rectangle, or circle (type quit to exit)? ")
    if shape.lower() == "square":
        length = float(input("Please input the side length for the square: "))
        area = compute_area_square(length)
        print(f"The area of the square is: {area:.2f}")        
    elif shape.lower() == "rectangle":
        width = float(input("Please input a width for the rectangle: "))
        length = float(input("Please input a length for the rectangle: "))
        area = compute_area_rectangle(width, length)
        print(f"The area of the rectangle is: {area:.2f}")
    elif shape.lower() == "circle":
        radius = float(input("Please input a radius for the circle: "))
        area = compute_area_circle(radius)
        print(f"The area of the circle is: {area:.2f}")        
    else:
        print("")

input("press ENTER to exit program")
    



