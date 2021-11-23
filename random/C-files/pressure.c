#include <stdio.h>
#include <inttypes.h>
#include <math.h>

uint32_t ilmanpaine(uint8_t xlsb, uint8_t lsb, uint8_t msb);
uint32_t apply_32_bits(uint32_t regi, uint32_t bits);
uint32_t apply_8_bits(uint32_t regi, uint8_t bits);
uint32_t move_bits(uint32_t regi, int steps);
uint8_t mask_xslb = 0b11110000;

/*
int main(){
    uint32_t paine = ilmanpaine(0b11011110, 0b10111100, 0b00011000); 
    printf("%zu", paine);
    return 0;
}
*/

uint32_t ilmanpaine(uint8_t xlsb, uint8_t lsb, uint8_t msb){
    uint32_t msb_regi = msb;
    uint32_t lsb_regi = lsb;
    uint32_t xlsb_regi = xlsb;
    uint32_t final_regi = 0;
    msb_regi = move_bits(msb_regi, 12);
    lsb_regi = move_bits(lsb_regi, 4);
    xlsb_regi = xlsb & mask_xslb;
    xlsb_regi = xlsb_regi >> 4;
    final_regi = apply_32_bits(final_regi, msb_regi);
    final_regi = apply_32_bits(final_regi, lsb_regi);
    final_regi = apply_32_bits(final_regi, xlsb_regi);
    return final_regi;

}


uint32_t apply_32_bits(uint32_t regi, uint32_t bits){
    uint32_t new_register = regi | bits;
    return new_register;
}


uint32_t apply_8_bits(uint32_t regi, uint8_t bits){
    uint32_t new_register = regi & bits;
    return new_register;
}

uint32_t move_bits(uint32_t regi, int steps){
    uint32_t new_register = regi << steps;
    return new_register;
}