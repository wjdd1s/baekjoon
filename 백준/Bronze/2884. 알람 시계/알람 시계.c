#include <stdio.h>

int main(void)
{
    int h, m;
    scanf("%d %d",&h, &m);

    if(m>=45)
        printf("%d %d", h, m-45);
    else if(m<45 && h>0)
        printf("%d %d", h-1, 15+m);
    else 
        printf("%d %d", 23, 15+m);

    return 0;
}