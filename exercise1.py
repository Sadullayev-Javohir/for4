row = int(input("Qator kiriting: "))
column = int(input("Ustun kiriting: "))

for i in range(1, row + 1):
    for j in range(1, column + 1):
        print("*", end = " ")
    print()