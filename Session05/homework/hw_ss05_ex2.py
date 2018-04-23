inventory = {
    'gold' : 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

#add new key 'pocket':
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print(inventory)

#remove 'dagger' from key 'backpack':
for key in inventory.keys():
    if key == 'backpack':
        inventory[key].remove('dagger')
print(inventory)

#add 50 to the value of 'gold':
for key in inventory.keys():
    if key == 'gold':
        inventory[key] += 50
print(inventory)
