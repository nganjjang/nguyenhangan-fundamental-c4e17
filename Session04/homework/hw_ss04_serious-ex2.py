print('''Guess your number game
Now think of a number from 0 to 100, then press 'Enter'
All you have to do is to answer to my guess
'c' if my guess is 'C'orrect
's' if my guess is 'S'maller than your number
'l' if my guess is 'L'arger than your number''')
lower = 0
upper = 100
answer = int((lower + upper) / 2)
loop = True
while loop:
    guess = input("Is {0} your number?".format(answer))
    if guess == "c":
        print("I knew it")
        loop = False
    elif guess == "s":
        lower = answer
        answer = int((lower + upper) / 2)
    elif guess == "l":
        upper = answer
        answer = int((lower + upper) / 2)
    else:
        loop = False
