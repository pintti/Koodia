#include <stdio.h>

int main(){
    int number, num_copy = 0;
    int numbers[5];
    scanf("%i", &number);
    num_copy = number;
    for(int i=4; i>=0; --i){
        int digit = number%10;
        numbers[i] = digit;
        number /= 10;
    }
    printf("Luku %i eroteltuna: %i %i %i %i %i", num_copy, numbers[0], numbers[1], numbers[2], numbers[3], numbers[4]);
    return 0;
}
