#include <stdio.h>
#include <inttypes.h>
#include <math.h>

float valoisuus(uint16_t rekisteri);
uint16_t move_bits(uint16_t reki, int steps);
uint16_t apply_mask(uint16_t reki, uint16_t mask);
uint16_t maskiE = 0b1111000000000000;
uint16_t maskiR = 0b0000111111111111;

/*
int main(){
    float lux = valoisuus(0b0110110000110101);
    printf("%f", lux);
    return 0;
}
*/

float valoisuus(uint16_t rekisteri){
    uint16_t e_registers = apply_mask(rekisteri, maskiE);
    uint16_t r_registers = apply_mask(rekisteri, maskiR);
    e_registers = move_bits(e_registers, 12);
    float lux = 0.01 * pow(2, e_registers) * r_registers;
    return lux;
}

uint16_t move_bits(uint16_t reki, int steps){
    uint16_t new_register = reki >> steps;
    return new_register;
}

uint16_t apply_mask(uint16_t reki, uint16_t mask){
    uint16_t new_register = reki & mask;
    return new_register;
}