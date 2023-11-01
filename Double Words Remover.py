string = str(input("Please tell a word:"))

def test():
    global x
    global y
    global z

    l = []
    m = []

    for x in string:
        l.append(x)
        m.append(x)

    x = 0
    y = 1
    z = len(l) - 1

    while x < z:
        if l[y] == l[x]:
            m[y] = "*"

        x += 1
        y += 1

    finalString = "".join(m)
    print(finalString)

test()
