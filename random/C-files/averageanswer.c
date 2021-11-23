#include <stdio.h>
#include <inttypes.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

float keskiarvo(char *lista);

/*int main(){
    char str[80] = "201,53,12,31,5";
    float avg = keskiarvo(str);
    return 0;
}*/

float keskiarvo(char *lista){
    char split[2] = ",";
    int length = 0;
    float sumlist[80];
    
    char *tok = strtok(lista, split);
    while(tok!=NULL){
        sumlist[length] = strtof(tok, NULL);
        length++;
        tok = strtok(NULL, split);
    }

    int p = 0;
    float float_length = length;
    float sum = 0;
    for(p=0; p<length; p++){
        sum = sum + sumlist[p];
    }
    float avg = sum/float_length;
    return avg;
}