'''n = int(input())
row = n
col = (2*row)-1
start, end = row-1, row-1
for i in range(row):
    for j in range(col):
        if (j>=start and j<=end):
            print("*", end="")
        else:
            print("", end=" ")
    print()
    start = start-1
    end = end+1'''


'''def circle(n):
    row = n
    col = n
    for i in range(row):
        for j in range(col):
            if (i==j or (i+j)==n-1):
                print(" ", end=" ")
            elif (i==0 or i==n-1 or j==0 or j==n-1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
circle(n)'''

'''char = "a"
n = int(input("Enter number of rows: "))
for i in range(n+1):
    for j in range(i):
        print(char, end=" ")
        char = chr(ord(char)+1)
        if (char > "z"):
            char = "a"
    print()'''

