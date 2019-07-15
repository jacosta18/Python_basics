# Dictionaries AKA Hashes
# Work with key: value pairs. As apposed to using indexes.

#Delcating a hash/dictionary
pika = {}

# Dictionaries work with key:values.

pika = {
    'name': 'Derik Dice',
    'pokemon':'pikachu',
    'age':17,
    'personality': 'Grumpy'
}

print(pika)

#Access information using the keys
print(pika['age'])
print(pika['pokemon'])

#re-assaign values using keys
pika['age'] = 18
print(pika['age'])

# Adding a key value pair

pika['colour']='Yellowish'
print(pika)

#Creating key value for first and last name
full_name=pika['name'].split()
print(full_name)
first_name = full_name[0]
print(first_name)
pika['first_name'] = first_name
pika ['last_name'] = full_name[1]
print(pika)

# Embedded data

pika = {
    'name': 'Derik Dice',
    'pokemon':'pikachu',
    'age':17,
    'personality':{
        'frumpy': 10,
        'lovely': 2}
}

print(pika['personality']['grumpy'])
print(pika['personality'][0])

# Important methods
keys = pika.keys()
print(keys)

values = pika.values()
print(values)




