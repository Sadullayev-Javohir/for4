col = int(input("Enter col: "))
row = int(input("Enter row: "))
add = 0
num = 0

for i in range(1, row + 1):
    for j in range(1, col + 1):
        num += 1
        if i >= j and i + j != row + 1:
            print(f"{num:02}", end=" ")
            add += num
    print()
print(add)