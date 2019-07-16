# Function
# Run blocks of code when called
# They shoukld be unitary / small
# They can take in arguments


# Function is like a machine.
#it can take in inputs
    # It can perform actions
    # It outputs different objects

# An argument is a function is like a variable that exists only in the scope of the function

# A function needs to be called to run it's code

# Syntax
# def name_function(arg1,arg2):
    # runs block of code

# Good Practices:
    # - Functions should be unitary / small jobs / one job
    # - Arguments should have good names
    # - Functions should be used to keep your code DRY
        # DRY - Don't Repeat Yourself
# Functions should return NOT print

# def say_hello():
#     print('Hello there')
#
# say_hello()

def full_name(f_name, l_name):  # These arguments can only be used inside the block of code.
    full_name_var= f_name + ' ' + l_name
    return full_name_var

print(full_name('Hamza', 'Danielson'))
















