# Control flow - IF statements
# Syntax - indentation matters
#if <condition>:
    # Block of code
# else:
    # Block of code
# else just print the false outcome

age = 70

if age >= 17:
    print('Your age is above 18, you can vote! :D')
elif age >= 18:
    print("You can do everything, just take it easy")
elif age >= 16:
    print('You can buy the lottery')
else:
    print('You are under age to vote')

########################################################

# weather = input("what's the weather like?").lower().strip()
#
# if weather == 'rainy' or weather == 'rainy':
#     print('take an unmbrela and a jacket')
# elif weather == 'sunny':
#     print('take glasses wear sunscreen')
# else:
#     print('Live your best life')

weather = input("what's the weather like?").lower().strip()

if weather == 'rainy and stormy':
    print('Take a jacket when it is rainy and stormy')
elif weather == 'foggy':
    print('Take an umbrella, because you never know')
elif weather == 'rainy':
    print('Take an umbrella only when it is rainy')
else:
    print('Live your best life')

