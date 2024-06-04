def generateMagicSquare(n):
    magicSquare = [[0] * n for x in range(n)]
    row, col = 0, n // 2
    num = 1
    while (num <= (n * n)):
        magicSquare[row][col] = num
        num += 1
        new_row, new_col = (row - 1) % n, (col + 1) % n
        if (magicSquare[new_row][new_col]):
            row = (row + 1) % n
        else:
            row, col = new_row, new_col
    return magicSquare

n = int(input("Enter the order of the magic square that must be odd: "))
if (n % 2 == 0):
    print("The order of the magic square must be odd.")
else:
    magicSquare = generateMagicSquare(n)
    print(f"Magic Square of order {n}:")
    for i in magicSquare:
        print(*i)