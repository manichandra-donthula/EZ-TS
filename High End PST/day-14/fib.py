def sum_fill_nth(n):
    pass

def nth_fibonacci_number(n):
    if n==1 or n==2:
        return n-1
    return nth_fibonacci_number(n+1) + nth_fibonacci_number(n)