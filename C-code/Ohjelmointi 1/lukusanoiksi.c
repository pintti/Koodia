#include <stdio.h>
#include <stdlib.h>

int returnNumber(int divider, int dividee);
void printNumber(int num);

int main(void){
    int get, thousands, hundreds, tens, singles;
    scanf("%d", &get);
    thousands = returnNumber(1000, get);
    if (thousands){
        if (thousands != 1){
            printNumber(thousands);
            printf("tuhatta");
        }
        else{
            printf("tuhat");
        }
    }
    get = get % 1000;
    hundreds = returnNumber(100, get);
    if (hundreds){
        if (hundreds != 1){
        printNumber(hundreds);
        printf("sataa");}
        else{
            printf("sata");
        }
    }
    get = get % 100;
    tens = returnNumber(10, get);
    if (tens){
        if (tens != 1){
        printNumber(tens);
        printf("kymmenta");}
        else{
            printf("kaksitoista");
            return 0;
        }
    }
    get = get % 10;
    singles = returnNumber(1, get);
    if (singles){
        printNumber(singles);
    }
    return 0;
}

int returnNumber(int divider, int dividee){
    int numOfDivs = 0;
    while (dividee >= divider){
        dividee -= divider;
        numOfDivs++;
    }
    return numOfDivs;
}

void printNumber(int num){
    switch (num)
    {
    case 1:
        printf("yksi");
        break;
    case 2:
        printf("kaksi");
        break;
    case 3:
        printf("kolme");
        break;
    case 4:
        printf("nelja");
        break;
    case 5:
        printf("viisi");
        break;
    case 6:
        printf("kuusi");
        break;
    case 7:
        printf("seitseman");
        break;
    case 8:
        printf("kahdeksan");
        break;
    case 9:
        printf("yhdeksan");
        break;
    }
}