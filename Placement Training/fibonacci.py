n = int(input("Enter number for fibanocci: "))

a = 0
b = 0
c = 0
if n == 0 or n == 1:
        c = 0
else:
    for i in range(1, n):
        c = a + b
        a = b
        b = i
        print(c)
# 0 1 1 2 3 5 8 13

# Recursion
'''def fibonacci(n):
    n1 = 0
    n2 = 1
    if n == 1:
        return n
    else:
        return 

print(fibonacci(n))'''