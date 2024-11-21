col = int(input("Enter col: "))
row = int(input("Enter row: "))
num = 0

for i in range(1, row + 1):
    for j in range(1, col + 1):
        if i >= j:
            print(f"{j:02}", end=" ")

    print()