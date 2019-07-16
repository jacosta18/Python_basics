# Swipe right

# swipe_choice = input("Will you swipe left or right?")
# answer = 'YES'
#
#
# if swipe_choice == 'right':
#     print("she swiped right too!:")
# while True:
#     print("she swiped right too!", answer)
#


# swipe_choice = input("Will you swipe left or right?")
# answer = 'YES'
#
# if swipe_choice == 'right':
#     print("she swiped right too!:")
#
# food_choice = input("What kind of food will you use?")
# if food_choice == 'italian':
#     print('Ah, molto bella!')
#
# if food_choice == 'curry':
#     print('Curry on a first DATE!? What were you thinking? GAME OVER')
#
# if
#

# while True:
#      print("she swiped right too!", answer)
#       else:
#      print("Hmm, perhaps Ollie's standards are a little high... GAME OVER")

while True:
    print("Welcome to the Game!")
    word = input("Will you swipe right or left")
    if word == 'right':
        print('She swiped right too!!')
    else:
        print("Hmm, perhaps Ollie's standards are a little high")
        break
    word_2 = input("What kind of food will you choose, Italian, Curry or Pub grub?")
    if word_2 == 'Italian':
        print('Ah! molto bella!')
    elif word_2 == 'Pub grub':
        print('Lovely jubbly')
    else:
        print("Curry on the first date!? What were you thinking?")
        break
    age = int(input("What age do you think she is?!"))
    if age <= 30:
        print("Pheww ... that was close")
    else:
        print("How dare you! ... ")
        break
    pay_choice = int(input("The bill is £100, will you pay for the full bill? Yes/No"))
    if pay_choice == 'Yes':
        print("How very gallant of you! She seems impressed")
    else:
        print("Nobody likes a cheapskate!!")
        break






