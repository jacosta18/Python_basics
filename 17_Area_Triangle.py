import math
# Area of a square
# def multiply(x, y):
#     return x * y

# Area of triangle
# def divide(x, y):
#     return x * y/2
#
#
# a = float(input("Enter the length of triangle: "))
# b = float(input("Enter the height of triangle: "))
#
# area = ((float(a) * float(b)) / 2)
#
# print(area)

#--------------------------------------------------------------------------#

##### Phase 1

def triangle_area(x,y):
    return ((x*y)/2)
print(triangle_area(20,2)==20)

##### Phase 2

def circle_area(radius):
    return math.pi * float(radius) ** 2
print(circle_area(23)==78.54)

#### Phase 3

def centimeters(inches,centimeters):
    return float(inches(25.4)) * float(1)
print(centimeters(25.4,1)==25.4)

