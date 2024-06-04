#include<stdio.h>
void main()
{
    int n, arr[100];
    printf("Enter size: ");
    scanf("%d",&n);
    for (int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    for (int i=0;i<n;i++){
        for (int j=i;j<n;j++){
            if (i==arr[j]){
                continue;
            }
            else {
                printf("%d", i);
                break;
            }
        }
    }
}