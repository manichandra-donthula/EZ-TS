from collections import deque
l=deque()
n = int(input("enter no of elements: "))
for i in  range(n):
    l.append(int(input("enter a element")))
print(l)
for i in range(n):
    print(l.popleft())

print(l)