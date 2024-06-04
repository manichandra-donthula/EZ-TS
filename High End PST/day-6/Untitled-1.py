arr=[16, 5, 2, 3, 18, 1]
def swap(a, b, flag):
    a, b =b, a
    flag = 1
    return a, b, flag
for i in range(len(arr)):
    flag = 0
    for j in range(len(arr)-i-1):
        if (arr[j]>arr[j+1]):
            arr[j], arr[j+1], flag = swap(arr[j], arr[j+1], flag)
    if (flag==0):
        break
print(arr)