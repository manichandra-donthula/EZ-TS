n = int(input())
'''x = 0
for i in range(1, n+1):
    x = x ^ i
print(x)'''
if n % 4 == 1:
    print(1)
if n % 4 == 2:
    print(n+1)
if n % 4 == 3:
    print(0)
if n % 4 == 0:
    print(n)
