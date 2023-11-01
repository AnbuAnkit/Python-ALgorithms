
word1 = str(input("Please enter a word:"))
word2 = str(input("Please enter another word:"))

def checker(str1, str2):
    global x
    global f

    x = 0
    f = 0

    global word1
    global word2

    word1 = word1.upper()
    word2 = word2.upper()

    string1 = sorted(word1)
    string2 = sorted(word2)

    if (len(string1)
            != len(string2)):
        print("False")
    else:

        while x < len(string1) - 1:
            if string1[x] != string2[x]:
                f += 1
            x += 1

        if f > 0:
            print("False")
        else:
            print("True")

checker(word1, word2)
