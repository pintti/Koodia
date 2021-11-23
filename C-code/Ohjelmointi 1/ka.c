#include <stdio.h>

int main(){
    double number, ka, sum, i = 0;
    scanf("%lf", &number);
    while(number>=0){
        sum += number;
        i++;
        scanf("%lf", &number);
    }
    ka = sum/i;
    printf("%.2lf", ka);

    return 0;
}