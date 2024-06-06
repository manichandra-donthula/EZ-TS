n = int(input())

'''
print(n*(n+1)//2)'''

# Recursion
def recursion_sum_n(n):
    if n == 1:
        return n
    else:
        return n + recursion_sum_n(n - 1)
    
print(recursion_sum_n(n))