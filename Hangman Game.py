import time

string = "ankit"
string = string.upper()

x = 0
c = 3

l = []
for i in string:
    l.append(i)

dash = []
while x < len(l) - 2:
    dash.append("_")
    x += 1
dash = "".join(dash)

print("Guess the correct word! \nYour hint is given below:")
print(l[0], dash, l[len(l) - 1], sep="")

#time.sleep(3)

response = str(input("Enter your answer:"))
response = response.upper()

def loop():
    global c

    if c == 0:
        print("Game over! Better luck next time!")
    else:
        if response != string:
            print("Wrong!")
            c += 1
            loop()
        else:
            print("You won! your answer was correct.")
loop()
