# Lists and Dictionaries
# List aka: array

# Sometimes we just need to list our crazy x-pokemons :)
# because we don't want work there

#This is how make a list
#[] separate items using,
# ['bananas', ,pine', 'gasoline']
#declaring a list and saving to variable
crazy_pokemons = ['Snorlax', 'Jigglipuff', 'Mewtoo']

print(crazy_pokemons)
print(type(crazy_pokemons))

# Lists are organised using indexes

#[0, 1, 2]
#[-3, -2, -1]
#['bananas', ,pine', 'gasoline']

print(len(crazy_pokemons))
print(crazy_pokemons[2])
print(crazy_pokemons[0])

#if you want to print the last in a list
#you have two options
    #array[len(array)-]
print(crazy_pokemons[len(crazy_pokemons)-1])
print(crazy_pokemons[-1])

# Re-assigning a value in a list, using the index
# We need to eveolve Mewtoo to Mewtree

print(crazy_pokemons)
crazy_pokemons[2] = 'Mewtree'
print(crazy_pokemons)

# Appeding a new pokemon
# We caught Pigeoto

crazy_pokemons.append('Pigeotto')
print(crazy_pokemons)

crazy_pokemons.insert(0, 'Rattata')
print(crazy_pokemons)

crazy_pokemons.insert(2, 'Squirtle')
print(crazy_pokemons)

# Remobing a record - using index

crazy_pokemons.pop()
print(crazy_pokemons)

crazy_pokemons.pop(0)
print(crazy_pokemons)

# Removing uding a filter
# crazy_pokemons.remove('Rattata')
# print(crazy_pokemons)

#Pop uses index and remove uses ('')
# Lists can have any data types

mixed_list = ['Jones', 10, 42, 'John']
print(mixed_list)
print(type(mixed_list[0]), type(mixed_list[1]))

#Inception List

leo_d = ['first', 2, ['leo'],'d']
print(leo_d[0])
print('accessing the index 2')
print(leo_d[2])
print(leo_d[2][1])

