import random

def range():

    global num1
    global num2

    num1 = int(input("Please enter a initial number:"))
    num2 = int(input("Please enter a final number:"))

    if num2 == num1 + 1:
        print("Range cant be this short.")
        range()
    else:
        print("You've got 3 chances to guess the correct answer, Good luck!")
range()

r = random.randint(num1 + 1, num2 - 1)
c = 2

def guessingGame():

    global num1
    global num2
    global r
    global c

    print("Range =", num1, "to", num2)
    response = int(input("Guess your number between the given range:"))

    if num1 > num2:
        print("Enter a valid range (Intial limit cannot be higher then Final limit)")
    else:
        if response < num1 or response > num2:
            print("Enter a value between the given range.")
            guessingGame()
        else:
            if c == 0:
                print("Game over! Better luck next time.")
            elif c == 1:
                print("LAST CHANCE!")
                c -= 1
                guessingGame()
            else:
                if response != r:
                    print("Wrong!")
                    c -= 1
                    guessingGame()
                else:
                    print("You won! Your answer is correct.")

guessingGame()
