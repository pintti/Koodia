#include <stdio.h>

int main(void){
    double fah;
    printf("%7s%12s\n", "Celsius", "Fahrenheit");
    for(int celc = -100; celc <= 100; celc+=10){
        fah = 1.8 * celc + 32;
        printf("%5d%12.2f\n", celc, fah);
    }
    return 0;
}