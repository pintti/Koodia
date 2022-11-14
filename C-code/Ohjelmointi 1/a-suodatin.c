#include <stdio.h>
#include <stdlib.h>

int main()
{
    char aku[5][100];
    for (int i=0; i<5; i++){
        printf("Anna merkkjono (max 100 merkkia) > ");
        scanf("%s", aku[i]);
    }
    for (int i=0; i<5; i++){
        if (aku[i][0] == 'a'){
            printf("\"a\"-merkilla alkava merkkijono \"%s\"\n", aku[i]);
        }
    }

    return 0;
}