#include <stdio.h>

int main(void){
    printf("%-7s%-7s%-7s%-7s\n","N", "10*N", "100*N", "1000*N");
    for (int i=1; i<=10; i++){
        printf("%-7d%-7d%-7d%-7d\n", i, 10*i, 100*i, 1000*i);
    }

    return 0;
}
