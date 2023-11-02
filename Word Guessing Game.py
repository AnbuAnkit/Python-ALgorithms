import random
import re

def nameChecker:
    name = str(input("Please enter a name:"))
    if len(name) < 2:
        print("Name cannot be this small, try somthing else")
        nameChecker()
nameChecker()

name = name.upper()
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
    response = response.upper()

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
