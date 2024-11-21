row = int(input("Enter row: "))
col = int(input("Enter column: "))
son = 0

for i in range(1, row + 1):
    for j in range(1, col + 1):
        son += 1
        print(son, end= " ")
    print()