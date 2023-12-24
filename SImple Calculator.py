int1 = int(input("Please enter a number:"))
int2 = int(input("Please enter another number:"))


def calculator():
    global int1
    global int2
    op = int(input(
        "Please specify the type of operation by integers given below:\n1. Addition\n2. Substraction\n3. Multiplication\n4. exponantial\n5. Modulos\n6. Division\nYour response:"))

    if op == 1:
        print(int1 + int2)
    elif op == 2:
        print(int1 - int2)
    elif op == 3:
        print(int1 * int2)
    elif op == 4:
        print(int1**int2)
    elif op == 5:
        print(int1%int2)
    elif op == 6:
        print(int1/int2)
    else:
        print("PLEASE ENTER A VALID OPERATION INTEGER.")
        calculator()
calculator()
