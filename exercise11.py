row = int(input("Qator kiriting: "))
column = int(input("Ustun kiriting: "))
orta = (row // 2) + 1

for i in range(1, row + 1):
    for j in range(1, column + 1):
        if i == j or i + j == row + 1:
            print("#", end = " ")
        else:
            print("*", end = " ")
    print()