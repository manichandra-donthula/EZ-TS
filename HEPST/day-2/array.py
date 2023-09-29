r=list(map(int, input("enter range sepearted by space:").split(" ")))
asize = int(input("enter array size"))
arr=[]
while(asize):
    a = int(input("enter a number"))
    if (a>=r[0] and a<=r[1]):
        arr.append(a)
        asize-=1
print("even numbers are: ")
for i in arr:
    if(i%2==0):
        print(i, end=" ")
#arrpow=[(2**x) for x in range(e)]
print("\n2 power values are:")
powarr=[(2**x) for x in range(r[1])]
for i in (powarr):
    if i in arr:
        print(i, end=" ") 