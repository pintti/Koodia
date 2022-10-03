#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void fillRanTable(int * table);

int main(void){
    int table[20];
    table[19] = -1;
    fillRanTable(table);

    for (int i=0; i<20; i++){
        printf("%d %d\n", i+1, table[i]+1);
    }

    return 0;
}

void fillRanTable(int *table){
    srand(time(NULL));
    int ranNum;
    int i = 0;
    int test;
    while (table[19] == -1){
        ranNum = rand() % 20;
        for (int k = 0; k <= i; k++){
            if (table[k] == ranNum){
                ranNum = -1;
            }
        }
        if (ranNum != -1){
            table[i] = ranNum;
            i++;
        }
    }
}