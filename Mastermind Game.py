
def checker():
    global plr1
    global plr2

    plr1 = 348
    if plr1 < 100 or plr1 > 999:
        print("Please enter a number given by the spacified range.")
        checker()

    plr2 = 456
    if plr2 < 100 or plr2 > 999:
        print("Please enter a number given by the specified range.")
        checker()
checker()

print(plr1)
