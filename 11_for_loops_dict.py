# For loops - Using dicttionaries / Hashes
# Suntax
# for <placeholder> in <dict>:
    #run block of code
#
# dict_data = {
#     'name':'Bronson',
#     'money': 200,
# }
# # We use the key to access the values of our dictionary
# # print(dict_data['name'])
#
# for key_place_holder in dict_data:
#     # When we iterate over a hash/dictionary.
#     # The placeholder, holds an individual key druing each iteration
#     print(key_place_holder)# This is the key :)
#     value = dict_data[key_place_holder] # user key and dictionary to extract individual values
#     print(value)
#
################################################

 # dict_data = {
 #     'name':'Bronson',
 #     'money': 200,
 # }
 # for key_place_holder in dict_data:
 #     print(key_place_holder +':',[key_place_holder])
 #

##################

dict_data = {
    'name':'Bronson',
    'money': 200,
}


embedded_dict_data = {
    1: {...},
    2: {...},
    3: {...}
}

for key in embedded_dict_data:
    print(embedded_dict_data[key])
    print(type(embedded_dict_data[key]))

print('///////')





embedded_dict_data = {
    1: {
    'name':'Bronson',
    'money': 200
    },
    2: {
    'name': 'Tania',
    'money': 300
    },
    3: {
    'name':'Tylor',
    'money': 400
    }
}

for item in embedded_dict_data.values():
    print(item)
    print(type(item))

