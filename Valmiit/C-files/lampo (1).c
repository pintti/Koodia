#include <stdio.h>
#include <inttypes.h>

float lampotila(uint16_t rekisteri, float kerroin);
/*
int main(){
    float tila = lampotila(0b0011001000000000, 0.03125);
    printf("%f", tila);
    return 0;
}
*/
float lampotila(uint16_t rekisteri, float kerroin){
    uint16_t irrottaja = 65532;
    uint16_t tila = rekisteri & irrottaja;
    tila = tila >> 2;
    float lampo = tila * kerroin;
    return lampo;
}