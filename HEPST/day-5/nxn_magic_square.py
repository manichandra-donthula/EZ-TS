def generate_magic_square(n):
    magic_square = [[0] * n for x in range(n)]
    row, col = 0, n // 2
    num = 1
    while (num <= n * n):
        magic_square[row][col] = num
        num += 1
        row, col = (row - 1) % n, (col + 1) % n
        if magic_square[row][col] != 0:
            row = (row + 1) % n
    return magic_square

n = int(input("Enter the order of the magic square that must be odd: "))
if (n % 2 == 0):
    print("The order of the magic square must be odd.")
else:
    magic_square = generate_magic_square(n)
    print(f"Magic Square of order {n}:")
    print(*magic_square)