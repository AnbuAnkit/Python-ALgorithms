#INITIANL INPUT
def intialInput():
    global plr1
    global plr2

    plr1 = int(input("Please enter a number player 1:"))
    if plr1 < 100 or plr1 > 999:
        print("Please enter a number given by the specified range.")
        intialInput()
intialInput()
#########

#DASH CONSTRUCTOR
strPlr1 = str(plr1)
dash = []
dupliDash = []
for i in strPlr1:
    dash.append(i)
    dupliDash.append(i)
#########

#CHECKER FUNCTION
plr1Counter = 0
plr2Counter = 0

def phase2():
    def intialInput2():
        global plr1
        global plr2

        plr1 = int(input("Please enter a number player 1:"))
        if plr1 < 100 or plr1 > 999:
            print("Please enter a number given by the specified range.")
            intialInput2()
    intialInput2()

    strPlr2 = str(plr2)
    dash = []
    dupliDash = []
    for i in strPlr2:
        dash.append(i)
        dupliDash.append(i)

    def checker2():

        global plr2Counter
        global plr1Counter
        global plr1
        global plr2

        def plr2input():
            global plr2

            plr2 = int(input("Your response?:"))
            if plr2 < 100 or plr2 > 999:
                print("Please enter a number given by the specified range.")
                plr2input()

        plr2input()

        if plr1 == plr2:
            print("Correct!")
        else:
            print("Wrong!")
            plr1Counter += 1
            print("Heres your hint, try again.")

            if plr1Counter == 1:
                x = 0
                while x < 2:
                    dash[x] = "_"
                    x += 1
                    string = "".join(dash)
                print(string)
                checker2()
            else:
                x = 0
                dupliDash[x] = "_"
                string = "".join(dupliDash)
                print(string)
                checker2()
    checker2()

def checker():
    global plr2Counter
    global plr1Counter
    global plr1
    global plr2


    def plr2input():
        global plr2

        plr2 = int(input("Your response?:"))
        if plr2 < 100 or plr2 > 999:
            print("Please enter a number given by the specified range.")
            plr2input()
    plr2input()

    if plr2 == plr1:
        print("Correct! Its player 2's turn now")
        phase2()
    else:
        print("Wrong!")
        plr2Counter += 1
        print("Heres your hint, try again.")

        if plr2Counter == 1:
            x = 0
            while x < 2:
                dash[x] = "_"
                x += 1
                string = "".join(dash)
            print(string)
            checker()
        else:
            x = 0
            dupliDash[x] = "_"
            string = "".join(dupliDash)
            print(string)
            checker()
checker()

if plr2Counter > plr1Counter:
    print("Player 1 won!")
elif plr2Counter == plr1Counter:
    print("Its a draw.")
else:
    print("Player 2 won!")
