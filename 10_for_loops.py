import time
#For loops in python
# Use to literate over collections
# Collections are lists and dict.

# We want to get an item at a time and do comething with it.

### Place holder is an internal variable that it's scope is limited to the loop.

# Syntax
# for <placeholder> in <list>:
    #run block of code


# x_crazy_landlords = ['Cruella de Vill', "Donal Duck", "Popeye the Maltese"]
#
# counter = 0
# print('starting loop')
#time.sleep (1)
# for land_l in x_crazy_landlords:
#     print('hello')
#     print(land_l)
#     print(counter)
#     counter += 1
#     time.sleep(3)
# print('loop ended')

# Excersice 1 -#####################################

#print  the same name of our landlords with nice formating.
#listing them using numbers

# x_crazy_landlords = ['Cruella de Vill', "Donal Duck", "Popeye the Maltese"]
#
# counter = 1
# for land_lord in x_crazy_landlords:
#     print(counter,'-', land_lord)
#     counter += 1

# Further loops ################################### listing numbers down in one line

# list_data =[1,2,3,4,5]
# embeded_list = [['1,2,3'],[5,6,7]]

# for num in list_data:
#     print(num)

# for data in embeded_list: # get the two lists
#        print(data)
#        for number in data:
#         print(number)
#         time.sleep(1)

# list_spartans = ['shav', 'adam','daniel','michael','omid','hamza','ally']
# embeded_list = [['shav', 'adam','daniel','michael'],['omid','hamza','ally']]
#
# for spartans in embeded_list:
#     for spartan in spartans:
#         print(spartan)
#
# list_spartans = ['shav', 'adam','daniel','michael','omid','hamza','ally']
#
# for spartan in list_spartans:
#     print('hello', spartan)

# list_scores = [1,10,3,4,5,6]
#
# for num in list_scores:
#     result_percent = num/10*100
#     print(result_percent)

# list_embed_scores =[[10,5,2],[3,4,6]]
#
# for ind_list in list_embed_scores:
#     print(ind_list)
#     for num in ind_list:
#         print(num*2)

