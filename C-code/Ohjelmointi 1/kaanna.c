#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int kaannaLuku(int luku);

int main(void){
    int luku = 0;
    scanf("%d", &luku);
    int revLuku = kaannaLuku(luku);
    printf("%d %d", luku, revLuku);
    return 0;
}

int kaannaLuku(int luku){
    int remainder, reverse = 0;
    while (luku != 0)
    {
        remainder = luku % 10;
        reverse = reverse * 10 + remainder;
        luku /= 10;
    }
    return reverse;
}
