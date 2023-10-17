#include <stdio.h>

int main(void)
{
    int n, i;
    int result = 0;
    scanf("%d", &n);

    for(i=1;i<10;i++)
    {
        result = n * i;
        printf("%d * %d = %d\n", n, i, result);
    }
    
    return 0;
}