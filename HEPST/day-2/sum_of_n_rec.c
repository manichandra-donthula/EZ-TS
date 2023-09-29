#include<stdio.h>
int add(int n){
    if (n<=0){
        return 0;
    }
    return n + add(n-1);
}

void main()
{
    int n = 9;
    printf("%d",add(n));
}