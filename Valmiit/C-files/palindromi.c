#include <stdio.h>
#include <inttypes.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

uint8_t palindromi(char *s, uint8_t length);

/*int main(){
    char str1[8] = "huhhuh";
    char str2[8] = "huhhoh";
    uint8_t length = 6;
    uint8_t nro1 = palindromi(str1, length);
    uint8_t nro2 = palindromi(str2, length);
    printf("Merkkijonolla %s funktio palauttaa %u\n", str1, nro1);
    printf("Merkkijonolla %s funktio palauttaa %u\n", str2, nro2);
}*/

uint8_t palindromi(char *s, uint8_t length){
    uint8_t jakaja = length/2;
    int i = 0;
    
    for(i=0; i<jakaja; i++){
        if(s[i] != s[length - 1 - i]){
            return i+1;
        }
    }
    return 0;
}