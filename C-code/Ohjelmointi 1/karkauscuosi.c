#include <stdio.h>
#include <stdlib.h>

int main(void){
    int year = 0;
    scanf("%d", &year);
    if (!(year % 4)){
        if ((year % 100) || (!(year % 400))){
            printf("Vuosi %d on karkausvuosi", year);
            return 0;
        }
    }
    printf("Vuosi %d ei ole karkausvuosi", year);
    return 0;
}