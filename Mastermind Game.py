
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

x = 0

dash = []
duplicatePlr1 = str(plr1)

for i in duplicatePlr1:
    dash.append(i)

while x < len(dash):
    int(dash[x])
    x += 1

for i in dash:
    print(type(i))

print(duplicatePlr1)

plr1Counter = 0
plr2Counter = 0

if plr2 == plr1:
    print("Correct! Now its player 1's chance to make guesses...")
else:
    print("Wrong!")
