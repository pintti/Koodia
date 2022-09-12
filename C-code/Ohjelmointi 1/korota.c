#include <stdio.h>
#include <stdlib.h>

int korotaKokonauslukuPotenssiin(int number, int powNum){
    int powed = number;
    for (int k = 1; k<powNum; k++){
        powed = powed * number;
    }
    return powed;
}

int main(void){
    int number = 0;
    int powNum = 0;
    int powed = 0;
    scanf("%d", &number);
    scanf("%d", &powNum);
    powed = korotaKokonauslukuPotenssiin(number, powNum);
    printf("%i %i %i", number, powNum, powed);
    return 0;
}