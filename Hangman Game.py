import time
import re

def stringChecker():
    global string
    string = str(input("Please enter your target word:"))

    if re.search("\ ", string) != None:
        print("Your word cannot contain spaces! or try to write a single word.")
        stringChecker()
stringChecker()
string = string.upper()

x = 0
c = 2

l = []
for i in string:
    l.append(i)

dash = []
while x < len(l) - 2:
    dash.append("_")
    x += 1
dash = "".join(dash)

print("Guess the correct word! you've got 3 chances. \nYour hint is:")
print(l[0], dash, l[len(l) - 1], sep="")

time.sleep(1)

def loop():
    global c

    response = str(input("Enter your answer:"))
    response = response.upper()

    if c == 0:
        print("Game over! Better luck next time!")
    else:
        if response != string:
            print("WRONG! Chances remaining:", c)
            c -= 1
            loop()
        else:
            print("You won! your answer was correct.")
loop()
