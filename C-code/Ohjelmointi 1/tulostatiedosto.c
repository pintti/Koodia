#include <stdio.h>
#include <stdlib.h>

int main(void){
    FILE *infile;
    infile = fopen("nimet.txt", "r");
    char string[20];
    int i = 0;

    if(!(infile)){
        printf("Tiedoston avaaminen epäonnistui");
        return 0;
    }

    while(fgets(string, sizeof(string), infile)){
        i = 0;
        while(string[i] != '\n'){
            if (string[i] == ';'){
                string[i] = ' ';
            }
            i++;
        }
        printf("%s\n", string);
    }

    fclose(infile);

    return 0;
}
