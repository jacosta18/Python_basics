# Booleans
#


var_true = True
var_false = False

print(type(var_true))
print(type(var_true))

# When we equate / evaluate something we get a boolean as a response
#Logical operator
# == / != / <> / >= / <=
weather = 'Rainy'

print(weather == 'sunny')
print(weather == 'Rainy')

#Logical **AND** & **OR**
# Evaluates two sides and both have to be true for it to return true

print(weather == 'Rainy' and weather == 'Sunny')
print(True and True)
# print(True and False)
print(weather == 'Rainy' and weather == 'Rainy')
print(True and False)

#Logical OR - One of the side equasion hace to be True to retrun True
print('>Testing logical or:')
print(True or False)
print(False or True)

# Some methods or function can return booleans
potential_number = '10'
print(potential_number.isnumeric())
#print(int(potential_number).isnumeric())

text = 'Hello World!'
print(text.startswith('H'))
print (text.startswith('h'))
print('Testing.endswith(arg)')
print(text[-1] == '?') # strings are list of characters. -1 represents the last index in said list.
print(text.endswith('!'))
print(text.endswith('?'))

# Booleans and numbers
print("printing bool values of numbers")
print(bool(0))
print(bool(13))
print(bool(1))
print(bool(3.14))

# Values of None
print(bool(None))

