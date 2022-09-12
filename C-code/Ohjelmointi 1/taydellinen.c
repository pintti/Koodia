#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int onkoLukuTaydellinen(int luku);

int main(void){
    for (int luku=1; luku<=10000; luku++){
        if(onkoLukuTaydellinen(luku)){
            printf("\nLuku %d on taydellinen luku", luku);
        }
    }  
    return(0);
}

int onkoLukuTaydellinen(int luku){
    int sum = 0;
    for (int i=1; i<luku; i++){
        if ((luku%i) == 0){
            sum += i;
        }
    }
    if (sum == luku){
        return 1;
    }
    return 0;
}
