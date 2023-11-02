import random

name = "Ankit"

l = []
r = random.randint(0, len(name) - 1)

for i in name:
    l.append(i)
randomLetter = l[r]

print(randomLetter)

