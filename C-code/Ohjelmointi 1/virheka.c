#include <stdio.h>
#include <stdlib.h>
#include <string.h>

double loop(){
    double number, sum = 0;
    int virhe = 0, i = 0;
    char str[30];
    char *ptr;
    while(1){
        scanf("%s", str);
        number = strtod(str, &ptr);
        if(strlen(ptr) != 0){
            printf("\n");
            for(int k=0; k<strlen(ptr); k++){
                printf("Ei ollut reaaliluku\n");
            }
            virhe++;
            printf("Virheellinen syote numero %d\n\n", virhe);
            if (virhe == 3){
                return 0;
            }
            printf("Ei kelpaa, yrita uudelleen! >");
        }
        else if(number < 0){
            return sum/i;
        }
        else{
            sum += number;
            i++;
        }
    }
}

int main(){
    double ka = 0;
    int virhe = 0;
    char str[30];
    printf("Anna reaaliluku ( negat arvo lopetaa) > ");
    ka = loop();
    if (ka){
        printf("%.2lf", ka);
    }
    else{
        printf("Virheellinen syote kolme kertaa. Ohjelma lopetetaan\n");
    }

    return 0;
}