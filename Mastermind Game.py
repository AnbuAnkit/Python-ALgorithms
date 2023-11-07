#INITIANL INPUT
def intialInput():
    global plr1
    global plr2

    plr1 = 348
    if plr1 < 100 or plr1 > 999:
        print("Please enter a number given by the spacified range.")
        intialInput()
intialInput()
#########



#DASH CONSTRUCTOR
strPlr1 = str(plr1)
dash = []

for i in strPlr1:
    dash.append(i)

#########



#CHECKER FUNCTION
plr1Counter = 0
plr2Counter = 0

def checker():
    global plr2Counter
    global plr1Counter
    global plr1
    global plr2

    x = 0

    def plr2input():
        global plr2

        plr2 = int(input("Your response?:"))
        if plr2 < 100 or plr2 > 999:
            print("Please enter a number given by the specified range.")
            plr2input()
    plr2input()

    if plr2 == plr1:
        print("Correct!")
    else:
        print("Wrong!")
        plr2Counter += 1
        print("Heres your hint, try again.")

        if plr2Counter == 1:
            while x <= 1:
                dash[x] = "_"
                x += 1
                string = "".join(dash)
            print(string)
        else:
            while x <= 2:
                dash[x] = "_"
                x += 1
                string = "".join(dash)
            print(string)
        checker()
checker()
#UNDER DEVELOPMENT#
