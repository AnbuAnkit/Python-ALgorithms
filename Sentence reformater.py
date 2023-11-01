sentence = str(input("Please enter a sentence to be reformated:"))

def converter(str):
    str = str.strip()

    l = []
    for i in str:
        l.append(i)

    x = 0
    y = 1

    l[0] = l[0].upper()
    while y < len(l):
        if l[x] == " " and l[y] != " ":
            l[y] = l[y].upper()
        else:
            l[y] = l[y].lower()

        x += 1
        y += 1

    str = ''.join(l)

    print(str)

converter(sentence)
