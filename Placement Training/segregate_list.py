'''arr = list(map(int, input().split()))
ev, od = [], []
for i in arr:
    if i%2==0:
        ev.append(i)
    else:
        od.append(i)
ev.sort()
od.sort()
arr = ev[::-1] + od
print(arr)'''

arr = list(map(int, input().split()))
seg = []
arr.sort()
for i in arr:
    if i%2==0:
        seg.insert(0, i)
    else:
        seg.append(i)
print(seg)
