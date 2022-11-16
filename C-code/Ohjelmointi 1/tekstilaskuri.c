#include <stdio.h>
#include <stdlib.h>

int main(void){
    FILE *infile;
    int ch, lines = 1, chars = 0;
    infile = fopen("teksti.txt", "r");

    if(!(infile)){
        printf("Tiedoston avaaminen epäonnistui");
        return 0;
    }
    for (ch=fgetc(infile); ch != EOF; ch=fgetc(infile)){
        if (ch == '\n'){
            lines++;
        }
        chars++;
    }
    fclose(infile);

    printf("\nRivit: %d\nMerkit: %d", lines, chars);

    return 0;
}
