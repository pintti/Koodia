#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main(void){
    srand(time(NULL));
    FILE *infile;
    infile = fopen("sanat.txt", "r");
    char word[20];

    if(!(infile)){
        printf("Tiedoston avaaminen epäonnistui");
        return 0;
    }

    randomizeWord(word, infile);
    printf("%s", word);

    fclose(infile);

    return 0;
}


void randomizeWord(char *string, FILE *infile){
    while(fgets(string, sizeof(string), infile)){
        if(rand()%5 == 0){
            return;
        }
    }
}

