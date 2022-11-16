#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
    FILE *infile;
    infile = fopen("sanakirja.txt", "r");
    char string[100], word[20], beforeSplit[10], *split;

    scanf("%s", word);

    if(!(infile)){
        printf("Tiedoston avaaminen epäonnistui");
        return 0;
    }

    while(fgets(string, sizeof(string), infile)){
        split = strtok(string, ";");
        //printf("Splitattu1 %s\n", split);
        if(!(strcmp(word, split))){
            split = strtok(NULL, "\n");
            printf("%s", split);
            fclose(infile);
            return 0;
        }
        else{
            strcpy(beforeSplit, split);
            split = strtok(NULL, "\n");
            //printf("Splitattu2 %s %s\n", split, beforeSplit);
            if(!(strcmp(word, split))){
                printf("%s", beforeSplit);
                fclose(infile);
                return 0;
            }
        }
    }

    fclose(infile);
    printf("Sanaa chaptre ei loytynyt sanakirjasta");
    return 0;
}
