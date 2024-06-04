def brute_force(n, arr):
    for i in range(1,  n+1):
        if i not in arr:
            return i

n = int(input())
arr = list(map(int, input().split()))[:n]

def xor_approach(n, arr):
    for i in range(1, n+1):
        ans = ans ^ i
        if (i != n):
            