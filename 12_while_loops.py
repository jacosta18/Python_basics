import time
# While loops

# Syntax
# While <condition>
    # Block of Code
    # ***Optional*** if <condition> break

counter = 0

while counter<28:
    print("let's go out! My ager is:",counter)
    counter += 1
    time.sleep(0.2)

print('end')

while True:
    print('Welcome to the loop')
    word = input('Tell me a word')
    if word == 'bananas':    #-------------------->Condition to go into the break key word
        print('you cracked the code')
        break               # -------------------->Safe word to break the loop.
    else:
        print("HAHAHAHA YOU FOOL. YOU WILL NEVER LEAVE")
        print("HAHAHAH")