row = int(input("Qator kiriting: "))
column = int(input("Ustun kiriting: "))


for i in range(1, row + 1):
    for j in range(1, column + 1):
        if (i % 2 == 0 and column % 2 == 0):
            print("1", end = " ")
        else:
            print("0", end = " ")
    print()