row = int(input("Enter row: "))
col = int(input("Enter col: "))
averagex = (row // 2) + 1
averagey = (col // 2) + 1
num = 0
add = 0

for i in range(1, row + 1):
    for j in range(1, col + 1):
        num += 1
        if j == 1 or i == averagex or j == averagey or j == col:
            add += num
            print(f"{num:02}", end=" ")
    print()
print(add)