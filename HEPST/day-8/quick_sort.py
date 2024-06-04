def quick_sort(arr):
    if (len(arr)<1):
        return arr
    else:
        pv = arr[0]
        left_arr = [i for i in arr[1:] if i<pv]
        right_arr = [i for i in arr[1:] if i>pv]
        return quick_sort(left_arr)+[pv]+quick_sort(right_arr)
arr = list(map(int, input().split()))
print(*quick_sort(arr))