import random

name = "Ankit"

l = []
r = random.randint(0, len(name) - 1)
c = 4

for i in name:
    l.append(i)

randomLetter = l[r]

def loop():
    global c
    global response

    response = str(input("Please enter a letter:"))

    if c == 0:
        print("Game over! Better luck next time.")
    elif c == 1:
        print("Last Chance!")
        c -= 1
        loop()
    else:
        if response != randomLetter:
            c -= 1
            print("Wrong!")
            loop()
        else:
            print("You won! Your answer is correct.")

loop()
