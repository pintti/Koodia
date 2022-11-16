#include <stdio.h>
#include <stdlib.h>

int main(void){
    FILE *infile1, *infile2;
    char infile1Name[30], infile2Name[30];
    scanf("%s", infile1Name);
    scanf("%s", infile2Name);

    infile1 = fopen(infile1Name, "r");
    infile2 = fopen(infile2Name, "r");

    if (infile1 == NULL || infile2 == NULL){
        printf("Tiedostojen avaaminen epäonnistui");
        return 0;
    }

    char ch1, ch2;
    ch1 = getc(infile1);
    ch2 = getc(infile2);

    while(ch1 != EOF && ch2 != EOF){
        if(ch1 != ch2){
            printf("Tiedostot eivät ole sisällöltään identtiset.");
            fclose(infile1);
            fclose(infile2);
            return 0;
        }
        ch1 = getc(infile1);
        ch2 = getc(infile2);
    }
    fclose(infile1);
    fclose(infile2);
    printf("Tiedostot ovat sisällöltään identtiset.");
    return 0;
}
