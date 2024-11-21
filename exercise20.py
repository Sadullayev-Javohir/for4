col = int(input("Enter col: "))
row = int(input("Enter row: "))

for i in range(1, row + 1):
    for j in range(1, col + 1):
        if i >= j:
            print("*", end=" ")

    print()