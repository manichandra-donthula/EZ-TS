n = int(input("Enter num: "))
k = int(input("Enter k: "))
t = n & (1<<k-1)
if (t == 0):
    print("not")
else:
    print("set")




'''
#Different approach
a = 10
k = 2
b = str(bin(a))[::-1]
if (b[k-1]=="1"):
    print("set")
else:
    print("not")'''