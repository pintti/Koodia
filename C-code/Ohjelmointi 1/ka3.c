#include <stdio.h>

int main(){
    double number, ka, sum, i = 0;
    scanf("%lf", &number);
    for(int k=0; k=10; k--){
        sum += number;
        i++;
        scanf("%lf", &number);
        if(number < 0){
            break;
        }
    }
    ka = sum/i;
    printf("%.2lf", ka);

    return 0;
}