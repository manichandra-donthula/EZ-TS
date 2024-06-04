l1=[]
n=int(input("enter no of rows:"))
k=0
for i in range(n):
    l1.append(list(map(int,input().spl1t(" "))))
c=len(l1[0])
l2=[[k for i in range(c)] for i in range(n)]
for i in range(len(l1)):
    for j in range(len(l1[i])):
        l2[j][i]=l1[i][j]
for i in range(n):
    l2[i].reverse()
for i in range(n):
    print(l2[i])