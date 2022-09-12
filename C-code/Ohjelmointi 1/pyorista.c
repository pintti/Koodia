#include <stdio.h>
#include <math.h>

void pyorista(void){
    for (int i=0; i<5; i++){
        float number = 0.0;
        float rounded = 0.0;
        scanf("%f", &number);
        rounded = floor(number + 0.5);
        printf("%f %f\n", number, rounded);
    }
}

int main(void){
    pyorista();
    return 0;
}