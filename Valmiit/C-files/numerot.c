#include <stdio.h>
#include <inttypes.h>
#include <math.h>

int64_t laske_kertoma(int8_t n);

/*int main(){
    int64_t numero = laske_kertoma(5);
    printf("%d", numero);
    return 0;
}*/

int64_t laske_kertoma(int8_t n){
    if (n > 20){
        return -1;
    }
    else {
        int64_t numero = 1;
        int8_t i;
        for (i=n; i>0; i--){
            numero = numero * i;
        }
        return numero;
    }
}