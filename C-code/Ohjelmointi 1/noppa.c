#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void diceSum(int * table, int sum);

int main(void){
    long numbers[11] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int rand1 = 0, rand2 = 0;
    srand(time(NULL));
    for (int i = 0; i<36000; i++){
        rand1 = rand() % 10;
        rand2 = rand() % 10;
        numbers[rand1+rand2]++;
    }

    for (int k=0; k<10; k++){
        printf("%d%3d\n", k+2, numbers[k]);
    }

    return 0;
}
