#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
    FILE *infile;
    int i = 0;
    char string[30], choice[10], fileName[10];
    scanf("%s", fileName);
    infile = fopen(fileName, "r");

    if(!(infile)){
        printf("Tiedoston avaaminen epäonnistui");
        return 0;
    }
    while(1){
        scanf("%s", choice);
        if (strcmp(choice, "Q") != 0){
            for (i=0; i<20; i++){
                if(fgets(string, sizeof(string), infile)){
                    printf("%s", string);
                }
                else{
                    return 0;
                }
            }
        }
        else{
            fclose(infile);
            return 0;
        }
    }
}