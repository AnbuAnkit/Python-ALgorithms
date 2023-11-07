#INITIANL INPUT
def intialInput():
    global plr1
    global plr2

    plr1 = 348
    if plr1 < 100 or plr1 > 999:
        print("Please enter a number given by the spacified range.")
        intialInput()

    plr2 = 456
    if plr2 < 100 or plr2 > 999:
        print("Please enter a number given by the specified range.")
        intialInput()
intialInput()
#########

#CODE UNDER DEVELOPMENT#



#DASH CONSTRUCTOR
parentDash = []

stringPlr1 = str(plr1)

for i in stringPlr1:
    parentDash.append(i)
dash = [int(i) for i in parentDash]
#########



#CHECKER FUNCTION
if plr2 == plr1:
    print("Correct!")
else:
    print("Wrong!")
    print("Here your hint, try again.")

#EXPERIMENT#
