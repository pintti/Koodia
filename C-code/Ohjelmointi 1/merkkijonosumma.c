#include <stdio.h>
#include <stdlib.h>

int main(void){
    char numC1[10], numC2[10];
    int num1, num2;
    printf("Anna 1. luku > ");
    fgets(numC1, sizeof(numC1), stdin);
    printf("Anna 2. luku > ");
    fgets(numC2, sizeof(numC2), stdin);

    sscanf(numC1, "%d", &num1);
    sscanf(numC2, "%d", &num2);

    printf("Lukujen %d ja %d summa on %d", num1, num2, num1+num2);

    return 0;
}