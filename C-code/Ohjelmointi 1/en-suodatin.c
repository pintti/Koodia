#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char aku[5][100];
    for (int i=0; i<5; i++){
        printf("Anna merkkjono (max 100 merkkia) > ");
        scanf("%s", aku[i]);
    }
    for (int i=0; i<5; i++){
        char one, two;
        one = aku[i][strlen(aku[i])-2];
        two = aku[i][strlen(aku[i])-1];
        if (one == 'e' && two == 'n'){
            printf("\"en\"-merkkijonoon paattyva merkkijono \"%s\"\n", aku[i]);
        }
    }

    return 0;
}
