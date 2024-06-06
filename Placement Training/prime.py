n=int(input())
count=0
for i in range(1, n):
    if n%i==0:
        count+=1
    if count>=2:
        break
if count < 2:
    print("Prime")
else:
    print("Composite")