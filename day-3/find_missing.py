#find out the smallest missing positive integer
arr = list(map(int, input().split(" ")))
m = max(arr)
f = 0
for i in range(m+1):
    if i not in arr:
        print(i)
        f = 1
        break
if (f == 0):
    print(m+1)