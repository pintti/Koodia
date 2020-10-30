#include <stdio.h>
#include <inttypes.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

void merkkilaskuri(char *str, uint8_t *tulos);

/*int main(){
    uint8_t tulos[2] = {0, 0};
    char str[80] = "Guinevere Squintest February Crucifixion";
    merkkilaskuri(str, tulos);
    printf("Vokaaleja on %i\n", tulos[0]);
    printf("Konsonantteja on %i\n", tulos[1]);
    return 0;
}*/

void merkkilaskuri(char *str, uint8_t *tulos){
    int i = 0;
    int vokaalit = 0;
    int konsonantit = 0;

    while(str[i] != '\0'){
        int letter = (int)str[i];
        if(letter >= 65 && letter < 90){
            if(letter == 65 || letter == 69 || letter == 73 || letter == 79 || letter == 85){
                vokaalit++;
            }
            else{
                konsonantit++;
            }
        }
        else if(letter >= 97 && letter < 122){
            if(letter == 97 || letter == 101 || letter == 105 || letter == 111 || letter == 117){
                vokaalit++;
            }
            else{
                konsonantit++;
            }
        }
    i++;
    }
    tulos[0] = vokaalit;
    tulos[1] = konsonantit;
}