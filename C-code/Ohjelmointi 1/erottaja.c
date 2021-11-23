#include <stdio.h>

int main(){
    int number = 0;
    char numbers[5];
    int multiply = 10000;
    scanf("%s", numbers);
    //sprintf(number, "%s", numbers);
    for(int i=0; i<5; i++){
        number = number + ((int)numbers[i] - 48) * multiply;
        multiply = multiply / 10;
    }
    printf("Luku %i on eroteltuna: %c %c %c %c %c", number, numbers[0], numbers[1], numbers[2], numbers[3], numbers[4]);
    return 0;
}
