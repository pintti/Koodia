#include <stdio.h>
#include <inttypes.h>
#include <math.h>

float kosteus(uint16_t rekisteri);
/*
int main(){
    float prosentti = kosteus(0b1000000000000000);
    printf("%f", prosentti);
    return 0;
}
*/
float kosteus(uint16_t rekisteri){
    float kosteus = ((rekisteri/pow(2, 16)) * 100);
    return kosteus;
}