n = int(input("Enter number: "))
'''# Normal approach for printing series upto Fn
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    a = 0
    b = 1
    fi = [a, b]
    for i in range(1, n):
        c = a + b
        a = b
        b = c
        fi.append(c)
print(*fi)'''

# Recursion for only printing Fn
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(n))