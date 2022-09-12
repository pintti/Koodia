#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int coinFlip(void);

int main(void){
    srand(time(NULL));
    int heads = 0; 
    int tails = 0;
    for(int i=0; i<100; i++){
        int flip = coinFlip();
        if (flip){
            tails++;
        }
        else{
            heads++;
        }
    }
    printf("Heittojen tulos: %d kruunua ja %d klaavaa", heads, tails);

    return 0;
}

int coinFlip(void){
    int ranNum = rand()%2;
    return ranNum;
}
