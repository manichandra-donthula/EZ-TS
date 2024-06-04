arr = list(map(int, input("Enter array elements seperated by space:").split(" ")))
ele = int(input("Enter element to be searched: "))
def linearSearch(arr, ele):
    flag = 0
    for i in arr:
        if(i==ele):
            flag = 1
    return flag
if(linearSearch(arr, ele)):
    print("Element is found in array")
else:
    print("Element is not found in array")