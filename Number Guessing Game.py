import random

num1 = 40
num2 = 50
r = random.randint(num1, num2)

print("Range =", num1, "to", num2)
response = int(input("Guess your number between the given range:"))

def game(r1, r2):
    global response
    global r
    c = 3

    if response < r1 or response > r2:
        print("Please enter a number within the range...")
    else:
        while c > 1:
            if response != r:
                c -= 1
                print("Wrong answer, try again!")
                game(r1, r2)
            else:
                print("Your answer is correct!")

    if c <= 0:
        print("Sorry but you have lost the game... better luck next time!")

game(num1, num2)

#print("Your range is", num1, "to", num2)

