#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void poistaValilyonnit(char *string1, char *string2);

int main(void){
    char uncleanString[20], clean[20], uncleanString2[20], clean2[20], uncleanString3[20], clean3[20];
    fgets(uncleanString, sizeof(uncleanString), stdin);
    fgets(uncleanString2, sizeof(uncleanString2), stdin);
    fgets(uncleanString3, sizeof(uncleanString3), stdin);
    poistaValilyonnit(uncleanString, clean);
    poistaValilyonnit(uncleanString2, clean2);
    poistaValilyonnit(uncleanString3, clean3);
    printf("%s\n%s\n%s\n", clean, clean2, clean3);

    return 0;
}


void poistaValilyonnit(char *string1, char *string2){
    int k = 0, i = 0;
    char *copy = string1; 
    while(copy[i] != '\0'){
        if (copy[i] != ' '){
            string2[k] = copy[i];
            k++;
        }
        i++;
    }
}
