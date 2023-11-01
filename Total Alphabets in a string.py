string = str(input("Please enter a word:"))

def checker(str):

    global x
    global i

    i = 0
    x = 0
    l = []

    for a in str:
        l.append(a)

    while x < len(str):

        if l[x] != " ":
            i += 1

        x += 1

    print("The total number of letters in the word is", i)

checker(string)
