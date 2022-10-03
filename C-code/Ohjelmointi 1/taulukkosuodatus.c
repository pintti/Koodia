#include <stdio.h>
#include <stdlib.h>

void checkNums(int *numArray);
void printNums(int *numArray);

int main(void){
    int num = 0;
    int numArray[20] = {0};
    for (int i=0; i<20; i++){
        printf("Syotä %d. luku >", i+1);
        scanf("%d", &num);
        if (!(num >= 20 && num <= 100)){
            while (!(num >= 10 && num <= 100))
            {
                printf("Yrita uudelleen > ");
                scanf("%d", &num);
            }
        }
        numArray[i] = num;
    }
    checkNums(numArray);
    printNums(numArray);
    return 0;
}

void checkNums(int *numArray){
    int i = 0, flag = 0;
    while (i<20){
        for (int k=i+1; k<20; k++){
            if (numArray[i] == numArray[k]){
                numArray[k] = 0;
                flag = 1;
            }
        }
        if (flag){
            numArray[i] = 0;
            flag = 0;
        }
        i++;
    }
}

void printNums(int *numArray){
    for (int i=0; i<20; i++){
        if (numArray[i] != 0){
            printf("%d\n", numArray[i]);
        }
    }
}
