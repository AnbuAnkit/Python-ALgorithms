import time

string = "ankit"
string = string.upper()

x = 0
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

time.sleep(3)

response = str(input("Enter your answer:"))
