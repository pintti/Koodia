#include <stdio.h>

int main(){
    double number, ka, sum, i = 0;
    do{
    scanf("%lf", &number);
    if(number >= 0){
        sum += number;
        i++;
        }
    }
    while(number >= 0);
    ka = sum/i;
    printf("%.2lf", ka);

    return 0;
}