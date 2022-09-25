#include <stdio.h>
#include <stdlib.h>

int main(void){
    int ten[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int insert[10];
    for (int i = 0; i<10; i++){
        printf("Syötä %d. luku >", ten[i]);
        scanf("%d", &insert[i]);
    }
    for (int i=0;i<10;i++){
        printf("%d %4d\n", insert[i], insert[9-i]);
    }
    return 0;
}