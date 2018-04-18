wlist = ["whiskey", "tonic", "martini", "mojito", "americano"]
from random import *
word = choice(wlist)
character_list = list(word)

print('''Guess your word game
Let's guess the following word:''')

for i in range (len(word)):
    random_character = choice(character_list)
    print(*random_character, end=" ")
    ind = character_list.index(random_character)
    character_list.pop(ind)
print()

loop = True
while loop:
    answer = input("Your answer: ")
    if answer == word:
        print("Hura")
        loop = False
    else:
        print("Guess again :(")
