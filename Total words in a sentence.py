
sentence = str(input("Please write your sentence here:"))

def checker(str):
    global x
    global y
    global c

    str = str.strip()

    l = []

    for i in str:
        l.append(i)

    x = 0
    y = 1
    c = 0

    while x < len(l):

        if y == len(l) and l[x] != " ":
            c += 1
        elif l[y] == " " and l[x] != " ":
            c += 1

        x += 1
        y += 1

    print("The total number of words in the sentence is:", c)

checker(sentence)
