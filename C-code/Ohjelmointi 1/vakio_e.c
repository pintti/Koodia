#include <stdio.h>

double summ(int i);

int main(void)
{
    // Tulosmuuttuja e
    double e=1.0;
    double sum = 0.0;
    int i = 1;
    while(i<=10){
        printf("\n%lf", e);
        e += summ(i);
        i++;
    }   
    printf("\n");
    return 0;
}

double summ(int i){
    int summed = 1;
    for (int k=1; k<=i; k++){
        summed = summed * k;
    }
    return (1.0/summed);
}