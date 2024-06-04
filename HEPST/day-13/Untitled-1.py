str1 = "BFFFBFBFFB"
str1len = len(str1)
visited = [0 for i in range(1000)]
cp = 0
visited[cp] = 1
count = 1
for ch in str1:
    if ch == "B":
        if cp-1>=0:
            cp-=1
    else:
        cp+=2
    if visited[cp]!=1:
        visited[cp]=1
        count+=1
print(count)
