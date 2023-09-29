arr = list(map(int, input("Enter array elements seperated by space:").split(" ")))
def sumarr(arr):
    total = 0
    for i in arr:
        total+=i
    return total
print("Sum of Array Elements: ", sumarr(arr))