# Creating a calculator

# def add(x, y):
#     return x + y
#
# def subtract(x, y):
#     return  x - y
#
# def multiply(x, y):
#     return x * y
#
# def divide(x, y):
#     return x / y
#
# print("select your option")
# print("1. Addition")
# print("2. Subtract")
# print("3. Mulitply")
# print("4. Divide")
#
# choice = input("Enter choice 1/2/3/4):")
#
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
#
# while True:
#     if choice == '1':
#         print(float(num1),"+", float(num2),"=", add(float(num1),float(num2)))
#     elif choice == '2':
#             print(float(num1), "-", float(num2), "=", subtract(float(num1),float(num2)))
#     elif choice == '3':
#             print (float(num1), "*", float(num2),"=", multiply(float(num1),float(num2)))
#     elif choice == '4':
#             print(float(num1), "/", float(num2), "=", divide(float(num1),float(num2)))
#     else:
#         print("Invalid input")
#     word = input("New operation? YES / NO:".lower())
#     if word == 'YES':
#         print("Let's GO!, PRESS CTRL,SHIFT, F10")
#     else:
#         print("See you later!")
#     break
#-----------------------------------------------------------------------------------------------

# This is an add function:

def multiply (x,y):
    return x*y

print(multiply(100,40)==4000)

# This is subtraction

def addition (x,y):
    return x+y
print(addition(20,5)==25)

# This is division

def subtraction(x,y):
    return x-y
print(subtraction(23,3)==20)

# This is division

def division(x,y):
    return x/y
print(division(50,5)==10)

#------------------------------------------------------------------------------

