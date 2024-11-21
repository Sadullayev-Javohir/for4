col = int(input("Enter col: "))
row = int(input("Enter row: "))
son = 1
add = 0
for i in range(1, row + 1):
    for j in range(1, col + 1):
        if j == 1 or j == col:
            add += son
            print(f"{son:02}", end=" ")
        son += 1
    print()
print(add)