col = int(input('Balandlik: '))
row = int(input('Uzunlik: '))

for i in range(1, row + 1):
    for j in range(1, col + 1):
        if i == 1 or j == 1 or j == col or i == row or i == j or i + j == row + 1:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print()
