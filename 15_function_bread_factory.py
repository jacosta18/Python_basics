# Our bread Factory

# Make dough

def make_dough(ingredient1,ingredient2):
    if 'wheat' in ingredient1 and 'water' in ingredient2:
        return 'dough'
    else:
        return 'wrong ingredient'

def bake_bread(semi_product):
    if semi_product == 'dough':
        return 'bread'
    else:
        return 'wrong ingredients used' + ingredient1 + ' ' + ingre

print(make_dough('wheat','water'))
print(make_dough('cement', 'water'))
print(make_dough('cement', 'water')) == 'cement'



# # Test
# print('call function make_dough, expect dough to be returned')
# print(make_dough('wheat','water') == 'dough')
#
# print(bake_bread ('dough') == 'bread')
# print(make_dough('cement', 'water') == 'wrong ingredients')
# print('called function make_dough with wrong ingredients. Expected it to be wrong')
#
# print('call function make_dough, expect dough to be returned')
# print(bake_bread('dough') == 'bread')

print('called function bake_bread with wrong ingredients. Expect outcome to be wrong ingredients')
print(bake_bread('chocolate cement') == 'wrong ingredients')
