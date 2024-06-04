def main():
    str1 = "madammadam"
    #a = int(input())
    n = len(str1)
    dp = [[0 for i in range(n)] for j in range(n)]
    i, j = 0, 0
    count = 0
    while (j<n):
        jflag = j
        while (jflag < n):
            if (i==jflag):
                dp[i][jflag] = 1
                count+=1
            elif (abs(i-jflag) == 1):
                if (str1[i]==str1[jflag]):
                    dp[i][jflag]=1
                    count+=1
                else:
                    dp[i][jflag]=0
            else:
                if (str1[i] == str1[jflag]):
                    if (dp[i+1][jflag-1]==1):
                        dp[i][jflag]=1
                        count+=1
                    else:
                        dp[i][jflag]=0
                else:
                    dp[i][jflag]=0
            i+=1
            jflag+=1
        j+=1
        i=0
    return count
print(main())