row = int(input("Enter row: "))
col = int(input("Enter column: "))
son = 1

if son % 2 == 1:

    for i in range(1, row + 1):
        for j in range(1, col + 1):
            print(son, end= " ")
            son += 2
        print()